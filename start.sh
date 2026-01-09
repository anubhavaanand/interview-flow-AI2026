#!/bin/bash
# Smart startup script for interview-flow-AI2026
# Handles port conflicts, environment setup, and clean shutdown

set -e

PROJECT_ROOT="/home/anubhavanand/Desktop/interview-flow-AI2026"
BACKEND_PORT=8000
FRONTEND_PORT=3000

echo "════════════════════════════════════════════════════════════"
echo "  interview-flow-AI2026 Startup Script"
echo "════════════════════════════════════════════════════════════"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to kill processes on ports
kill_port() {
    local port=$1
    local name=$2
    
    if lsof -i :$port > /dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Port $port ($name) is in use. Cleaning up...${NC}"
        lsof -i :$port | awk 'NR!=1 {print $2}' | xargs kill -9 2>/dev/null || true
        sleep 2
        echo -e "${GREEN}✅ Cleaned up port $port${NC}"
    fi
}

# Function to setup environment
setup_env() {
    echo -e "\n${BLUE}📋 Setting up environment...${NC}"
    
    if [ -f "$PROJECT_ROOT/backend/.env" ]; then
        echo -e "${GREEN}✅ Found .env file${NC}"
        source "$PROJECT_ROOT/backend/.env" || true
    else
        echo -e "${YELLOW}⚠️  No .env file found${NC}"
        echo "   Create one at: backend/.env"
        echo "   Template available at: backend/.env.example"
    fi
    
    # Export for current session
    export PROJECT_ROOT
    export BACKEND_PORT
    export FRONTEND_PORT
}

# Function to start backend
start_backend() {
    echo -e "\n${BLUE}🚀 Starting Backend (FastAPI)...${NC}"
    
    kill_port $BACKEND_PORT "Backend"
    
    cd "$PROJECT_ROOT/backend"
    
    # Check if venv exists
    if [ ! -d "venv" ]; then
        echo -e "${YELLOW}Creating virtual environment...${NC}"
        python3 -m venv venv
    fi
    
    # Activate venv and start
    source venv/bin/activate
    
    # Check if dependencies installed
    if ! python -c "import fastapi" 2>/dev/null; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        pip install -q -r requirements.txt
    fi
    
    # Start the server
    echo -e "${GREEN}✅ Backend starting on port $BACKEND_PORT${NC}"
    nohup python -m uvicorn main:app --host 0.0.0.0 --port $BACKEND_PORT > /tmp/backend.log 2>&1 &
    BACKEND_PID=$!
    echo "Backend PID: $BACKEND_PID"
    
    # Wait for startup
    sleep 3
    
    # Verify it's running
    if curl -s http://localhost:$BACKEND_PORT/ > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Backend is running!${NC}"
        return 0
    else
        echo -e "${RED}❌ Backend failed to start${NC}"
        cat /tmp/backend.log
        return 1
    fi
}

# Function to start frontend
start_frontend() {
    echo -e "\n${BLUE}🚀 Starting Frontend (React)...${NC}"
    
    kill_port $FRONTEND_PORT "Frontend"
    
    cd "$PROJECT_ROOT/frontend"
    
    # Check if node_modules exists
    if [ ! -d "node_modules" ]; then
        echo -e "${YELLOW}Installing npm dependencies...${NC}"
        npm install --quiet
    fi
    
    # Start the server
    echo -e "${GREEN}✅ Frontend starting on port $FRONTEND_PORT${NC}"
    BROWSER=none nohup npm start > /tmp/frontend.log 2>&1 &
    FRONTEND_PID=$!
    echo "Frontend PID: $FRONTEND_PID"
    
    # Wait for startup
    sleep 8
    
    # Verify it's running
    if curl -s http://localhost:$FRONTEND_PORT/ > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Frontend is running!${NC}"
        return 0
    else
        echo -e "${RED}❌ Frontend failed to start${NC}"
        echo "Check logs: tail -f /tmp/frontend.log"
        return 1
    fi
}

# Function to show status
show_status() {
    echo -e "\n${BLUE}📊 Service Status:${NC}"
    echo "════════════════════════════════════════════════════════════"
    
    if curl -s http://localhost:$BACKEND_PORT/ > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Backend${NC}: http://localhost:$BACKEND_PORT"
    else
        echo -e "${RED}❌ Backend${NC}: Not running"
    fi
    
    if curl -s http://localhost:$FRONTEND_PORT/ > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Frontend${NC}: http://localhost:$FRONTEND_PORT"
    else
        echo -e "${RED}❌ Frontend${NC}: Not running"
    fi
    
    echo "════════════════════════════════════════════════════════════"
}

# Function to stop services
stop_services() {
    echo -e "\n${YELLOW}Stopping services...${NC}"
    kill_port $BACKEND_PORT "Backend"
    kill_port $FRONTEND_PORT "Frontend"
    echo -e "${GREEN}✅ Services stopped${NC}"
}

# Main script execution
main() {
    case "${1:-start}" in
        start)
            setup_env
            start_backend || exit 1
            start_frontend || exit 1
            show_status
            echo -e "\n${GREEN}🎉 All services started!${NC}"
            echo -e "${BLUE}📖 Access the application:${NC}"
            echo "   Frontend: http://localhost:$FRONTEND_PORT"
            echo "   Backend:  http://localhost:$BACKEND_PORT"
            echo -e "\n${YELLOW}Logs:${NC}"
            echo "   Backend: tail -f /tmp/backend.log"
            echo "   Frontend: tail -f /tmp/frontend.log"
            ;;
        stop)
            stop_services
            ;;
        restart)
            stop_services
            sleep 2
            $0 start
            ;;
        status)
            show_status
            ;;
        logs)
            case "${2:-both}" in
                backend)
                    tail -f /tmp/backend.log
                    ;;
                frontend)
                    tail -f /tmp/frontend.log
                    ;;
                both)
                    echo "Backend logs:"
                    tail -f /tmp/backend.log &
                    echo ""
                    echo "Frontend logs:"
                    tail -f /tmp/frontend.log
                    ;;
            esac
            ;;
        *)
            echo "Usage: $0 {start|stop|restart|status|logs}"
            echo ""
            echo "Commands:"
            echo "  start         - Start backend and frontend"
            echo "  stop          - Stop all services"
            echo "  restart       - Restart all services"
            echo "  status        - Show service status"
            echo "  logs [type]   - Show logs (backend|frontend|both)"
            exit 1
            ;;
    esac
}

# Run main function
main "$@"

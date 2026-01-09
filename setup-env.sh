#!/bin/bash
# Setup environment variables for Azure OpenAI integration
# Run this once to configure your credentials

set -e

PROJECT_ROOT="/home/anubhavanand/Desktop/interview-flow-AI2026"
ENV_FILE="$PROJECT_ROOT/backend/.env"
ENV_EXAMPLE="$PROJECT_ROOT/backend/.env.example"

echo "════════════════════════════════════════════════════════════"
echo "  Azure OpenAI Environment Setup"
echo "════════════════════════════════════════════════════════════"

# Check if .env already exists
if [ -f "$ENV_FILE" ]; then
    echo "✅ .env file already exists at: $ENV_FILE"
    echo ""
    echo "Current content:"
    cat "$ENV_FILE" | grep -v '^#' | grep -v '^$' || echo "   (empty or comments only)"
    echo ""
    read -p "Do you want to update it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping setup."
        exit 0
    fi
fi

echo ""
echo "📝 Please provide your Azure OpenAI credentials:"
echo ""

read -p "Azure OpenAI API Key (AZURE_OPENAI_KEY): " API_KEY
if [ -z "$API_KEY" ]; then
    echo "❌ API Key is required!"
    exit 1
fi

read -p "Azure OpenAI Endpoint (AZURE_OPENAI_ENDPOINT): " ENDPOINT
if [ -z "$ENDPOINT" ]; then
    echo "❌ Endpoint is required!"
    exit 1
fi

# Validate endpoint format
if [[ ! $ENDPOINT =~ https:// ]]; then
    echo "❌ Endpoint should start with https://"
    exit 1
fi

read -p "Azure OpenAI Deployment Name [gpt-4] (optional): " DEPLOYMENT
DEPLOYMENT=${DEPLOYMENT:-gpt-4}

# Create .env file
cat > "$ENV_FILE" << EOF
# Azure OpenAI Configuration
# Generated: $(date)

AZURE_OPENAI_KEY=$API_KEY
AZURE_OPENAI_ENDPOINT=$ENDPOINT
AZURE_OPENAI_DEPLOYMENT=$DEPLOYMENT

# Backend Configuration
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend Configuration
FRONTEND_HOST=localhost
FRONTEND_PORT=3000
EOF

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ Environment setup complete!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📁 Configuration saved to: $ENV_FILE"
echo ""
echo "🚀 Next steps:"
echo "   1. Run: ./start.sh"
echo "   2. Open http://localhost:3000"
echo "   3. Go to /interview and submit code"
echo "   4. You should see AI feedback!"
echo ""
echo "⚠️  Important: Never commit .env to git!"
echo ""

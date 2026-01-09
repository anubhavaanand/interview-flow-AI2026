#!/bin/home/anubhavanand/Desktop/interview-flow-AI2026/backend/.env/bash
# Setup environment variables for GitHub Models
# Run this once to configure your GitHub token

set -e

PROJECT_ROOT="/home/anubhavanand/Desktop/interview-flow-AI2026"
ENV_FILE="$PROJECT_ROOT/backend/.env"
ENV_EXAMPLE="$PROJECT_ROOT/backend/.env.example"

echo "════════════════════════════════════════════════════════════"
echo "  GitHub Models Environment Setup"
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
echo "📝 Please provide your GitHub Models token:"
echo ""
echo "💡 To get a token:"
echo "   1. Go to: https://github.com/settings/tokens"
echo "   2. Click 'Generate new token' → 'Fine-grained personal access token'"
echo "   3. Give it a name and select 'ai_model' permission"
echo "   4. Copy the token and paste it below"
echo ""

read -sp "GitHub Token (GITHUB_TOKEN): " GITHUB_TOKEN
if [ -z "$GITHUB_TOKEN" ]; then
    echo ""
    echo "❌ GitHub Token is required!"
    exit 1
fi

echo ""
echo ""

# Create .env file
cat > "$ENV_FILE" << EOF
# GitHub Models Configuration
# Generated: $(date)

GITHUB_TOKEN=$GITHUB_TOKEN

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

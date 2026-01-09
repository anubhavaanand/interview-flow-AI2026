# Frontend for interview-flow-AI2026

React-based frontend for the AI-powered DSA interview coach.

## Setup

```bash
cd frontend
npm install
npm start
```

The app will start on `http://localhost:3000`

## Pages

- **Home** (`/`) - Landing page with "Start Mock Interview" button
- **Interview** (`/interview`) - Problem display + code editor
- **Feedback** (`/feedback`) - AI-generated feedback
- **Dashboard** (`/dashboard`) - Stats and progress tracking

## API Integration

The frontend communicates with the backend API at `http://localhost:8000`:
- `GET /problem` - Fetch DSA problem
- `POST /analyze` - Submit code for analysis

## Build

```bash
npm run build
```

Outputs to `build/` directory.

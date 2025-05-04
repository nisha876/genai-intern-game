# genai-intern-game
🔧 Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/genai-intern-game.git
cd genai-intern-game

2. Install Docker & Docker Compose
Ensure you have Docker Desktop installed and running.

3. Start the Application
docker compose up --build

This launches:
a. A FastAPI backend (uvicorn main:app)
b. A React-based frontend
c. PostgreSQL database
d. Redis cache

4. Access the Game
Open your browser and go to: http://localhost:8000/play/


🎮 How to Play
a. Start a game by clicking “Start Game”.
b. You’ll be prompted to interact with a GenAI-powered assistant to solve logic-based challenges.
c. Responses are scored, and points accumulate.
d. Your progress is stored per session and limited via rate limiting to ensure fairness.


🏗️ Architectural Choices
a. Frontend: Built using React for a dynamic user experience.
b. Backend: FastAPI was chosen for its speed and support for asynchronous operations.
c. Database: PostgreSQL for persistence of user sessions and scores.
d. Cache: Redis for quick access to game state, prompt history, and rate limiting.


✨ Prompt Design
Prompts are structured to:
a. Guide the user step-by-step.
b. Evaluate reasoning and creativity.
c. Ensure the assistant replies within bounded logic and scoring parameters.

Prompts include metadata (difficulty, category) to adaptively scale with player progress.

![Screenshot 2025-05-05 003031](https://github.com/user-attachments/assets/ef808a85-c1ef-48c5-9278-de15b7b8b4ab)

![Screenshot 2025-05-05 003143](https://github.com/user-attachments/assets/baf0d8f9-8dbc-4023-a4bb-84f46043b128)


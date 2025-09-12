# Full-Stack Autonomous Call Center Management System

This repository contains the scaffold for a full-stack autonomous call center management system. It includes a Python backend with FastAPI, a Next.js frontend, and integration with services like MongoDB and Qdrant, all orchestrated with Docker Compose.

## Project Architecture

The project is structured as a monorepo with three main directories:

-   `backend/`: A FastAPI application that serves the REST APIs and contains all the business logic.
-   `frontend/`: A Next.js (TypeScript) application that provides the user interface for monitoring and management.
-   `scripts/`: Intended for utility and setup scripts. (Currently empty).

The entire stack is designed to be run via Docker, providing a consistent and isolated development environment.

### Backend Services

-   **Framework**: FastAPI
-   **Orchestration**: LangGraph for building the LLM agent.
-   **LLM**: Google Gemini (via API).
-   **Database**: MongoDB for structured data like call logs.
-   **Vector Search**: Qdrant for semantic search (e.g., FAQ matching).
-   **Blockchain**: A mock blockchain logger to create an immutable audit trail of interactions.
-   **Authentication**: JWT-based security for API endpoints.

### Frontend Services

-   **Framework**: Next.js with TypeScript.
-   **UI Kit**: Shadcn/ui built on top of Tailwind CSS for a modular and accessible design.
-   **Features**: Stubs for a live dashboard, interaction logs, and an escalation management queue.

## Getting Started

### Prerequisites

-   [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
-   A Google Gemini API key.

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create the root environment file:**
    Copy the example environment file and fill in your details.
    ```bash
    cp .env.example .env
    ```
    Open the `.env` file and add your `GEMINI_API_KEY`. The other variables can remain as their default values for the local Docker setup.

3.  **Build and run the services:**
    From the root of the project, run the following command:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images for the backend and frontend and start all the services (`backend`, `frontend`, `mongo`, `qdrant`).

4.  **Access the applications:**
    -   **Backend API**: The API will be available at `http://localhost:8000`. You can access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.
    -   **Frontend UI**: The web interface will be running at `http://localhost:3000`.

### Development

-   The backend and frontend services are configured with hot-reloading. Any changes you make to the source code in the `backend/` or `frontend/` directories on your local machine will automatically trigger a reload of the respective service inside Docker.
-   To stop all the running services, press `Ctrl+C` in the terminal where `docker-compose` is running, or run `docker-compose down` from another terminal.

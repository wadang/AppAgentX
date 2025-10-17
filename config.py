"""Configuration module that reads runtime settings from environment variables."""

import os

from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
# These settings control the connection and behavior of the Large Language Model API
# Please fill in your own API information below

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "")
# Base URL for the LLM API service, using a proxy to access OpenAI's API
# Please enter your LLM service base URL here

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
# API key for authentication with the LLM service
# Please enter your LLM API key here

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
# Specific LLM model version to be used for inference
# You can use OpenAI models like "gpt-4o" or DeepSeek models like "deepseek-chat"

LLM_MAX_TOKEN = int(os.getenv("LLM_MAX_TOKEN", "1500"))
# Maximum number of tokens allowed in a single LLM request

LLM_REQUEST_TIMEOUT = int(os.getenv("LLM_REQUEST_TIMEOUT", "500"))
# Timeout in seconds for LLM API requests

LLM_MAX_RETRIES = int(os.getenv("LLM_MAX_RETRIES", "3"))
# Maximum number of retry attempts for failed LLM API calls

# LangChain Configuration
# Settings for LangChain integration and monitoring
# Uncomment and fill in the following settings if you need LangSmith functionality

LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false")
# Enables LangSmith tracing for debugging and monitoring

LANGCHAIN_ENDPOINT = os.getenv(
    "LANGCHAIN_ENDPOINT",
    "https://api.smith.langchain.com",
)
# Endpoint URL for LangSmith API services

LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")
# API key for authentication with LangSmith services
# Please enter your LangSmith API key here if needed

LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "")
# Project name for organizing LangSmith resources

# Neo4j Configuration
# Settings for connecting to the Neo4j graph database
# Please update these settings according to your Neo4j installation

Neo4j_URI = os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687")
# URI for connecting to the Neo4j database server
# Default is localhost, change if your database is hosted elsewhere

Neo4j_AUTH = (
    os.getenv("NEO4J_USER", "neo4j"),
    os.getenv("NEO4J_PASSWORD", "12345678"),
)
# Authentication credentials (username, password) for Neo4j
# Please update with your actual Neo4j credentials

# Feature Extractor Configuration
# Settings for the feature extraction service
# Please ensure this service is running at the specified address

Feature_URI = os.getenv("FEATURE_URI", "http://127.0.0.1:8001")
# URI for the feature extraction service API
# Default is localhost port 8001, update if needed

# Screen Parser Configuration
# Settings for the screen parsing service
# Please ensure this service is running at the specified address

Omni_URI = os.getenv("OMNI_URI", "http://127.0.0.1:8000")
# URI for the Omni screen parsing service API
# Default is localhost port 8000, update if needed

# Vector Storage Configuration
# Settings for the vector database used for embeddings storage
# Please fill in your vector database information

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
# API key for authentication with Pinecone vector database service
# Please enter your Pinecone API key here

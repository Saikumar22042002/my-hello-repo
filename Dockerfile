# Stage 1: Builder - Install dependencies into a virtual environment
FROM python:3.11-slim AS builder

WORKDIR /app

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final - Create the production image
FROM python:3.11-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY app.py .

# Set the path to include the venv
ENV PATH="/opt/venv/bin:$PATH"

# Run as a non-root user for security
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Use gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers=4", "app:app"]

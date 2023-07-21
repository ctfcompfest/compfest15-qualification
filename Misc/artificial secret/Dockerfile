# Use an official Ubuntu 18.04 as a parent image
FROM ubuntu:18.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3.7 python3-pip && \
    python3.7 -m pip install --upgrade pip

# Copy the current directory contents into the container at /usr/src/app
COPY src .

# Install python libraries
RUN python3.7 -m pip install openai discord.py

# When the container launches, this is the command that will be run.
CMD ["python3.7", "main.py"]

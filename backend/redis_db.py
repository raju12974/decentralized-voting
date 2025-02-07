import redis
import config
import json

redis_client = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

def get_candidates():
    candidates_json = redis_client.get("candidates")
    if candidates_json:
        return json.loads(candidates_json)
    return []

def add_candidates():
    candidates = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    redis_client.set("candidates", json.dumps(candidates))

def add_candidate(name):
    # Retrieve existing candidates
    candidates_json = redis_client.get("candidates")
    candidates = json.loads(candidates_json) if candidates_json else []

    if any(candidate["name"].lower() == name.lower() for candidate in candidates):
        return {"error": "Candidate with this name already exists!"}

    # Generate new id based on the length of the list
    new_id = len(candidates) + 1

    # Append new candidate
    new_candidate = {"id": new_id, "name": name}
    candidates.append(new_candidate)

    # Store updated list back in Redis
    redis_client.set("candidates", json.dumps(candidates))

    return new_candidate

# Uncomment this to add candidates initially
# add_candidates()
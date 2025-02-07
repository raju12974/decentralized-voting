def create_vote(candidate_id, voter_id):
    return {"candidate_id": candidate_id, "voter_id": voter_id}

def get_results(blockchain):
    results = {}
    for block in blockchain.chain:
        for transaction in block['transactions']:
            candidate_id = transaction['candidate_id']
            if candidate_id not in results:
                results[candidate_id] = 0
            results[candidate_id] += 1
    return results

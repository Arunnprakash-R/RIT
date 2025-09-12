import json
import hashlib
import datetime

class MockBlockchainLogger:
    def __init__(self, log_file="blockchain_log.txt"):
        """
        Initializes the mock blockchain logger.
        In a real implementation, this would connect to a Solana client.
        """
        self.log_file = log_file
        print("Mock Blockchain Logger initialized.")

    def _calculate_hash(self, data: str):
        """Calculates a SHA-256 hash for a given string."""
        return hashlib.sha256(data.encode()).hexdigest()

    async def log_interaction(self, session_id: str, user_query: str, ai_response: str):
        """
        Logs an interaction to a local file, simulating an immutable ledger entry.
        Each log entry contains a hash of the previous entry to form a chain.
        """
        timestamp = datetime.datetime.utcnow().isoformat()

        # Get the hash of the last block to chain them together
        last_hash = ""
        try:
            with open(self.log_file, "r") as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    last_block = json.loads(last_line)
                    last_hash = last_block['hash']
        except FileNotFoundError:
            # This is the first entry (genesis block)
            pass

        # Create the block data
        block_data = {
            "session_id": session_id,
            "user_query": user_query,
            "ai_response": ai_response,
            "timestamp": timestamp,
            "previous_hash": last_hash,
        }

        # Create the hash of the current block's data
        block_string = json.dumps(block_data, sort_keys=True)
        current_hash = self._calculate_hash(block_string)

        # Finalize the block with its own hash
        final_block = {
            "hash": current_hash,
            "data": block_data,
        }

        # "Mine" the block by writing it to the log file
        with open(self.log_file, "a") as f:
            f.write(json.dumps(final_block) + "\n")

        print(f"Logged interaction for session {session_id} to mock blockchain. Hash: {current_hash}")
        return current_hash

# Instantiate the logger for use in the application
blockchain_logger = MockBlockchainLogger()

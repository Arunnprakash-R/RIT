class MockEmailDispatcher:
    def __init__(self):
        """
        Initializes the mock email dispatcher.
        A real implementation would use a client like SendGrid or Amazon SES.
        """
        print("Mock Email Dispatcher initialized.")

    async def send_email(self, to_address: str, subject: str, body: str):
        """
        Simulates sending an email by printing the details to the console.
        """
        print("--- Sending Mock Email ---")
        print(f"To: {to_address}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        print("--------------------------")
        return {"status": "success", "message_id": "mock_message_id"}

    async def send_escalation_email(self, escalation_details: dict):
        """
        A specific method for sending escalation notifications.
        """
        session_id = escalation_details.get("session_id", "N/A")
        reason = escalation_details.get("reason", "No reason provided.")

        subject = f"Escalation Alert: Session {session_id}"
        body = f"""
        An interaction has been escalated.

        Session ID: {session_id}
        Reason: {reason}

        Please review the case in the supervisor dashboard.
        """
        # In a real app, this would be a configured recipient list
        to_address = "supervisor@example.com"

        await self.send_email(to_address, subject, body)

# Instantiate the dispatcher for use in the application
email_dispatcher = MockEmailDispatcher()

from .utils import generate_random_hex, generate_key_pair

class TLSServer:
    def __init__(self):
        self.server_random = None
        self.selected_cipher = None
        self.certificate = None

    def process_client_hello(self, client_data):
        """Step 2: Server Hello"""
        self.server_random = generate_random_hex()
        # Select the first cipher suite offered by client
        self.selected_cipher = client_data['cipher_suites'][0]
        self.certificate = generate_key_pair() # Simulating sending a Cert

        return {
            "msg_type": "Server Hello",
            "version": "TLS 1.3",
            "server_random": self.server_random,
            "cipher_suite": self.selected_cipher,
            "certificate": "BEGIN CERTIFICATE...\n(Verified by CA)\n...END CERTIFICATE"
        }
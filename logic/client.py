from .utils import generate_random_hex

class TLSClient:
    def __init__(self):
        self.client_random = None
        self.cipher_suites = [
            "TLS_AES_128_GCM_SHA256",
            "TLS_AES_256_GCM_SHA384",
            "TLS_CHACHA20_POLY1305_SHA256"
        ]
        self.session_id = None

    def send_client_hello(self):
        """Step 1: Client Hello"""
        self.client_random = generate_random_hex()
        self.session_id = generate_random_hex(16)
        
        return {
            "msg_type": "Client Hello",
            "version": "TLS 1.3",
            "client_random": self.client_random,
            "session_id": self.session_id,
            "cipher_suites": self.cipher_suites
        }

    def generate_pre_master_secret(self):
        """Step 3: Client Key Exchange simulation"""
        return generate_random_hex(48)
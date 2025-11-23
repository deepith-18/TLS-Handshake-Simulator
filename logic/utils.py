import os
import binascii
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_random_hex(length=32):
    """Generates a random hex string (simulating a Nonce)."""
    return binascii.hexlify(os.urandom(length)).decode('utf-8')

def generate_key_pair():
    """Simulates generating a Public/Private key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    
    # Convert to PEM format for display purposes
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    return pem_public

def simulate_encryption(data):
    """Simulates encrypting data (visual simulation)."""
    return f"ENCRYPTED[{binascii.hexlify(data.encode()).decode('utf-8')[:20]}...]"
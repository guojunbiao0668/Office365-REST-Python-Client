from office365.runtime.client_value import ClientValue


class ChangeNotificationEncryptedContent(ClientValue):
    """Represents the encrypted data attached to a change notification."""

    def __init__(self, data=None, data_key=None, data_signature=None, encryption_certificate_id=None,
                 encryption_certificate_thumbprint=None):
        """
        :param str data: Base64-encoded encrypted data that produces a full resource represented as JSON.
            The data has been encrypted with the provided dataKey using an AES/CBC/PKCS5PADDING cipher suite.
        :param str data_key: ase64-encoded symmetric key generated by Microsoft Graph to encrypt the data value and
            to generate the data signature. This key is encrypted with the certificate public key that was provided
            during the subscription. It must be decrypted with the certificate private key before it can be used
            to decrypt the data or verify the signature. This key has been encrypted with the following cipher
            suite: RSA/ECB/OAEPWithSHA1AndMGF1Padding.
        :param str data_signature: Base64-encoded HMAC-SHA256 hash of the data for validation purposes.
        :param str encryption_certificate_id: ID of the certificate used to encrypt the dataKey.
        :param str encryption_certificate_thumbprint: Hexadecimal representation of the thumbprint of the certificate
             used to encrypt the dataKey
        """
        self.data = data
        self.dataKey = data_key
        self.dataSignature = data_signature
        self.encryptionCertificateId = encryption_certificate_id
        self.encryptionCertificateThumbprint = encryption_certificate_thumbprint

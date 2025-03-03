"""TLS ClientHello packages from Wireshark."""

# yapf: disable

TLS_1_0: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0x68, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x64,  # Length
        0x03, 0x01, # Version: TLS 1.0
        # Random
        0x4e, 0x55, 0xde, 0x32, 0x80, 0x07, 0x92, 0x9f,
        0x50, 0x41, 0xe4, 0xf9, 0x58, 0x32, 0xfc, 0x4f,
        0x10, 0xb3, 0xde, 0x44, 0x4d, 0xa9, 0x67, 0x78,
        0xea, 0xd1, 0x5f, 0x29, 0x09, 0x04, 0xc1, 0x06,
        0x00, # Session ID Length
        0x00, 0x28, # Cipher Suites Length
            0x00, 0x39,
            0x00, 0x38,
            0x00, 0x35,
            0x00, 0x16,
            0x00, 0x13,
            0x00, 0x0a,
            0x00, 0x33,
            0x00, 0x32,
            0x00, 0x2f,
            0x00, 0x05,
            0x00, 0x04,
            0x00, 0x15,
            0x00, 0x12,
            0x00, 0x09,
            0x00, 0x14,
            0x00, 0x11,
            0x00, 0x08,
            0x00, 0x06,
            0x00, 0x03,
            0x00, 0xff,
        0x02, # Compression Methods
            0x01,
            0x00,
        0x00, 0x12, # Extensions Length
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
])


TLS_1_2: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0x48, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x42, # Length
        0x03, 0x03, # Version: TLS 1.2
        # Random
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0x00, # Session ID Length
        0x00, 0x04, # Cipher Suites Length
            0x00, 0x01, # NULL-MD5
            0x00, 0xff, # RENEGOTIATION INFO SCSV
        0x01, # Compression Methods
            0x00, # NULL
        0x00, 0x17, # Extensions Length
            # Extension
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
            # Extension
            0x00, 0x0f, # Extension Type: Heart Beat
            0x00, 0x01, # Length
            0x01, # Mode: Peer allows to send requests
])


TLS_1_2_ORDER: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0x48, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x42, # Length
        0x03, 0x03, # Version: TLS 1.2
        # Random
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0x00, # Session ID Length
        0x00, 0x04, # Cipher Suites Length
            0x00, 0x01, # NULL-MD5
            0x00, 0xff, # RENEGOTIATION INFO SCSV
        0x01, # Compression Methods
            0x00, # NULL
        0x00, 0x17, # Extensions Length
            # Extension
            0x00, 0x0f, # Extension Type: Heart Beat
            0x00, 0x01, # Length
            0x01, # Mode: Peer allows to send requests
            # Extension
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
])


TLS_1_2_MORE: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0x47, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x41, # Length
        0x03, 0x03, # Version: TLS 1.2
        # Random
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0x00, # Session ID Length
        0x00, 0x04, # Cipher Suites Length
            0x00, 0x01, # NULL-MD5
            0x00, 0xff, # RENEGOTIATION INFO SCSV
        0x01, # Compression Methods
            0x00, # NULL
        0x00, 0x16, # Extensions Length
            # Extension
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
            # Extension
            0x00, 0x23, # Extension Type: Session Ticket TLS
            0x00, 0x00, # Length
])


TLS_1_0_OLD: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0xec, # Length 104
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0xe8,  # Length 100
        0x03, 0x01, # Version: TLS 1.0
        # Random
        0x4e, 0x55, 0xde, 0x32, 0x80, 0x07, 0x92, 0x9f,
        0x50, 0x41, 0xe4, 0xf9, 0x58, 0x32, 0xfc, 0x4f,
        0x10, 0xb3, 0xde, 0x44, 0x4d, 0xa9, 0x67, 0x78,
        0xea, 0xd1, 0x5f, 0x29, 0x09, 0x04, 0xc1, 0x06,
        0x00, # Session ID Length
        0x00, 0x28, # Cipher Suites Length
            0x00, 0x39,
            0x00, 0x38,
            0x00, 0x35,
            0x00, 0x16,
            0x00, 0x13,
            0x00, 0x0a,
            0x00, 0x33,
            0x00, 0x32,
            0x00, 0x2f,
            0x00, 0x05,
            0x00, 0x04,
            0x00, 0x15,
            0x00, 0x12,
            0x00, 0x09,
            0x00, 0x14,
            0x00, 0x11,
            0x00, 0x08,
            0x00, 0x06,
            0x00, 0x03,
            0x00, 0xff,
        0x02, # Compression Methods
            0x01,
            0x00,
        0x00, 0x96, # Extensions Length 18 + 4 + 132 = 150
            0x00, 0x15, # Extension Type: Padding
            0x00, 0x80, # Length
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
                0xde, 0xad, 0xbe, 0xef, 0xde, 0xad, 0xbe, 0xef,
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
])


SSL_3_0: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x00, # Version: SSL 3.0
    0x00, 0x7f, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x7b, # Length
        0x03, 0x00, # Version: SSL 3.0
        # Random
        0x53, 0x11, 0x25, 0xc2, 0x92, 0xd6, 0xca, 0xf1,
        0x79, 0x90, 0xba, 0x38, 0x8f, 0xad, 0xc8, 0x13,
        0xa3, 0x1b, 0x57, 0xd9, 0xf4, 0x3e, 0xd2, 0x8b,
        0xb6, 0x5e, 0xe3, 0x12, 0xca, 0x81, 0x2f, 0xc5,
        0x00, # Session ID Length
        0x00, 0x54, # Cipher Suites Length
            0xc0, 0x14,
            0xc0, 0x0a,
            0xc0, 0x22,
            0xc0, 0x21,
            0x00, 0x39,
            0x00, 0x38,
            0xc0, 0x0f,
            0xc0, 0x05,
            0x00, 0x35,
            0xc0, 0x12,
            0xc0, 0x08,
            0xc0, 0x1c,
            0xc0, 0x1b,
            0x00, 0x16,
            0x00, 0x13,
            0xc0, 0x0d,
            0xc0, 0x03,
            0x00, 0x0a,
            0xc0, 0x13,
            0xc0, 0x09,
            0xc0, 0x1f,
            0xc0, 0x1e,
            0x00, 0x33,
            0x00, 0x32,
            0xc0, 0x0e,
            0xc0, 0x04,
            0x00, 0x2f,
            0xc0, 0x11,
            0xc0, 0x07,
            0xc0, 0x0c,
            0xc0, 0x02,
            0x00, 0x05,
            0x00, 0x04,
            0x00, 0x15,
            0x00, 0x12,
            0x00, 0x09,
            0x00, 0x14,
            0x00, 0x11,
            0x00, 0x08,
            0x00, 0x06,
            0x00, 0x03,
            0x00, 0xff,
        0x01, # Compression Methods
            0x00,
])


SSL_2_0: bytes = bytes([
    0x80, 0x67, # Length (leading bit set)
    0x01, # Handshake Type: Client Hello
    0x03, 0x01, # Version
    0x00, 0x4e, # Cipher spec length
    0x00, 0x00, # Session ID length
    0x00, 0x10, # Challenge length
        # Cipher Suites
        0x00, 0x00, 0x39,
        0x00, 0x00, 0x38,
        0x00, 0x00, 0x35,
        0x00, 0x00, 0x16,
        0x00, 0x00, 0x13,
        0x00, 0x00, 0x0a,
        0x07, 0x00,
        0xc0, 0x00,
        0x00, 0x33,
        0x00, 0x00, 0x32,
        0x00, 0x00, 0x2f,
        0x03, 0x00,
        0x80, 0x00,
        0x00, 0x05,
        0x00, 0x00, 0x04,
        0x01, 0x00,
        0x80, 0x00,
        0x00, 0x15,
        0x00, 0x00, 0x12,
        0x00, 0x00, 0x09,
        0x06, 0x00,
        0x40, 0x00,
        0x00, 0x14, 0x00,
        0x00, 0x11, 0x00,
        0x00, 0x08, 0x00,
        0x00, 0x06, 0x04,
        0x00, 0x80, 0x00,
        0x00, 0x03, 0x02,
        0x00, 0x80, 0x00,
        0x00, 0xff,
        # Session ID
        0x74, 0x15, 0xdc, 0x11, 0x0b, 0xcb, 0x2b, 0x03,
        0x5d, 0xb1, 0x5a, 0x2f, 0xac, 0x72, 0x45, 0x2e,
])


BAD_DATA1: bytes = bytes([
    0x16, 0x03, 0x01, 0x00, 0x68, 0x01, 0x00, 0x00,
    0x64, 0x03, 0x01, 0x4e, 0x4e, 0xbe, 0xc2, 0xa1,
    0x21, 0xad, 0xbc, 0x28, 0x33, 0xca, 0xa1, 0xd6,
    0x6e, 0x57, 0xb9, 0x1f, 0x8c, 0x19, 0x0e, 0x44,
    0x16, 0x9e, 0x7d, 0x20, 0x35, 0x4b, 0x65, 0xb2,
    0xc0, 0xd5, 0xa8, 0x00, 0x00, 0x28, 0x00, 0x39,
    0x00, 0x38, 0x00, 0x35, 0x00, 0x16, 0x00, 0x13,
    0x00, 0x0a, 0x00, 0x33, 0x00, 0x32, 0x00, 0x2f,
    0x00, 0x05, 0x00, 0x04, 0x00, 0x15, 0x00, 0x12,
    0x00, 0x09, 0x00, 0x14, 0x00, 0x11, 0x00, 0x08,
    0x00, 0x06, 0x00, 0x03, 0x00, 0xff, 0x02, 0x01,
    0x00, 0x00, 0x12, 0x00, 0x00, 0x00, 0x0e, 0x00,
])


BAD_DATA2: bytes = bytes([
    0x16, 0x03, 0x01, 0x00,
])


TLS_1_2_BAD: bytes = bytes([
    # TLS record
    0x16, # Content Type: Handshake
    0x03, 0x01, # Version: TLS 1.0
    0x00, 0x48, # Length
        # Handshake
        0x01, # Handshake Type: Client Hello
        0x00, 0x00, 0x42, # Length
        0x03, 0x03, # Version: TLS 1.2
        # Random
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        0x00, # Session ID Length
        0x00, 0x04, # Cipher Suites Length
            0x00, 0x01, # NULL-MD5
            0x00, 0xff, # RENEGOTIATION INFO SCSV
        0x01, # Compression Methods
            0x00, # NULL
        0x00, 0x17, # Extensions Length
            # Extension
            0x00, 0x00, # Extension Type: Server Name
            0x00, 0x0e, # Length
            0x00, 0x0c, # Server Name Indication Length
                0x00, # Server Name Type: host_name
                0x00, 0x09, # Length
                # "localhost"
                0x6c, 0x6f, 0x63, 0x61, 0x6c, 0x68, 0x6f, 0x73, 0x74,
            # Extension
            0x00, 0x0f, # Extension Type: Heart Beat
            0x00, 0x01, # Length
            0x01, # Mode: Peer allows to send requests
])

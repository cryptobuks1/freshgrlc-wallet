
GRLC = {
    'name':                 'Garlicoin',
    'ticker':               'GRLC',
    'database': {
        'name':             'grlc'
    },
    'coindaemon': {
        'hostname':         'garlicoind',
        'port':             42068
    },
    'address_version':      38,
    'privkey_version':      176,
    'segwit_info': {
        'addresstype':      'base58',
        'address_version':  73,
        'send_only':        True
    }
}


TGRLC = {
    'name':                 'Garlicoin Testnet',
    'ticker':               'tGRLC',
    'database': {
        'name':             'tgrlc'
    },
    'coindaemon': {
        'hostname':         'garlicoind-testnet',
        'port':             42070
    },
    'address_version':      111,
    'privkey_version':      239,
    'segwit_info':          None
}


TUX = {
    'name':                 'Tuxcoin',
    'ticker':               'TUX',
    'database': {
        'name':             'tux'
    },
    'coindaemon': {
        'hostname':         'tuxcoind',
        'port':             42072
    },
    'address_version':      65,
    'privkey_version':      193,
    'segwit_info': {
        'addresstype':      'bech32',
        'address_prefix':   'tux',
        'send_only':        False
    }
}


KEYSEEDER = {
    'name':                 'Keyseeder',
    'ticker':               None,
    'database':             None,
    'coindaemon': {
        'hostname':         'keyseeder',
        'port':             GRLC['coindaemon']['port']
    },
    'address_version':      GRLC['address_version'],
    'privkey_version':      GRLC['privkey_version'],
    'segwit_info':          None
}


DATABASE_PROTOCOL   = 'mysql+pymysql'
DATABASE_HOST       = 'mariadb'
DATABASE_WALLET_DB  = 'wallets'
ENCRYPTION_KEY      = '00112233445566778899aabbccddeeff'


DATABASE_CREDENTIALS    = ('wallet', 'databasepassword')
COINDAEMON_CREDENTIALS  = ('rpc', 'rpcpassword')
KEYSEEDER_CREDENTIALS   = ('rpc', 'rpcpassword')


COINS = [ GRLC, TUX, TGRLC ]


API_ENDPOINT = ''
INDEXER_API_ENDPOINT = ''
INDEXER_ADDRESS_API_PATH = '/address'
httpie-adobeio
==============

AdobeIO plugin for `HTTPie <https://httpie.org/>`_.

It currently provides support for Adobe IO service authentication


Installation
------------

.. code-block:: bash

    $ pip install httpie-adobeio


You should now see ``adobeio`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

.. code-block:: bash

    $ http --auth-type=adobeio --auth='client-key:client-secret' https://cloudmanager.adobe.io/api/programs


You can also use `HTTPie sessions <https://httpie.org/doc#sessions>`_:

.. code-block:: bash

    # Create session
    $ http --session=logged-in --auth-type=adobeio --auth='profile:client-secret' https://cloudmanager.adobe.io/api/programs

    # Re-use auth
    $ http --session=logged-in https://cloudmanager.adobe.io/api/programs

The plugin will look for a configuration file in the `~/.httpie_adobeio.ini` location:
.. code-block:: toml
    [DEFAULT]
    ims_base=https://ims-na1.adobelogin.com

    public_cert=-----BEGIN CERTIFICATE-----
     your public certificate here
     important: note leading indentation
     -----END CERTIFICATE-----

    private_key=-----BEGIN PRIVATE KEY-----
     your key private key here 
     important: note leading indentation
     -----END PRIVATE KEY-----

    [profile-1]
    ims_org=ABC123@AdobeOrg
    account_id=ABC123@techacct.adobe.com
    api_key=ABC123ABC123ABC123ABC123ABC123
    scopes=ent_cloudmgr_sdk



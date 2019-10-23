httpie-adobeio
==============

AdobeIO plugin for `HTTPie <https://httpie.org/>`_ that provides support for `Adobe IO service account authentication <https://www.adobe.io/authentication/auth-methods.html#!AdobeDocs/adobeio-auth/master/AuthenticationOverview/ServiceAccountIntegration.md/>`_.


Installation
------------

.. code-block:: bash

    $ pip install httpie-adobeio


You should now see ``adobeio`` under ``--auth-type`` in ``$ http --help`` output.


Configuration
-------------

The plugin will look for a configuration file in the `~/.httpie_adobeio.ini` location:
.. code-block:: 

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
           ent_campaign_sdk

Shared settings can be saved in the ``DEFAULT`` section.  It's possible to have multiple profiles and reference them from username part of the ``--auth`` parameter



Usage
-----

.. code-block:: bash

    $ http --auth-type=adobeio --auth='profile:client-secret' https://cloudmanager.adobe.io/api/programs


You can also use `HTTPie sessions <https://httpie.org/doc#sessions>`_:

.. code-block:: bash

    # Create session
    $ http --session=logged-in --auth-type=adobeio --auth='profile:client-secret' https://cloudmanager.adobe.io/api/programs

    # Re-use auth
    $ http --session=logged-in https://cloudmanager.adobe.io/api/programs





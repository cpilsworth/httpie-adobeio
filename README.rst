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

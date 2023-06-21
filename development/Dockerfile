FROM netboxcommunity/netbox:v3.5.4

COPY . /tmp/build/

# install plugins
RUN \
    echo "**** installing plugins ****" \
    && /opt/netbox/venv/bin/pip install --no-warn-script-location \
    qrcode \
    pillow \
    netbox-inventory \
    /tmp/build/

# cleanup installation
RUN \
    echo "**** cleanup ****" \
    && apt-get purge --auto-remove -y \
    && apt-get clean \
    && rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# activate plugins
ARG SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy"
COPY development/config/plugins.py /etc/netbox/config/plugins.py
RUN \
    echo "**** activating plugins ****" \
    && /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input

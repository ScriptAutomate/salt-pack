{% import "setup/redhat/map.jinja" as buildcfg %}

include:
{% if buildcfg.build_release == 'rhel7' %}

    - pkg.libsodium.1_0_5.rhel7
    - pkg.openpgm.5_2_122.rhel7
    - pkg.python-chardet.2_2_1.rhel7
    - pkg.python-cherrypy.3_2_2.rhel7
    - pkg.python-crypto.2_6_1.rhel7
    - pkg.python-enum34.1_0.rhel7
    - pkg.python-futures.3_0_3.rhel7
    - pkg.python-impacket.0_9_14.rhel7
    - pkg.python-ioflo.1_3_8.rhel7
    - pkg.python-libcloud.0_20_0.rhel7
    - pkg.python-libnacl.1_4_3.rhel7
    - pkg.python-msgpack.0_4_6.rhel7
    - pkg.python-pyzmq.15_3_0.rhel7
    - pkg.python-raet.0_6_5.rhel7
    - pkg.python-requests.2_6_0.rhel7
    - pkg.python-simplejson.3_3_3.rhel7
    - pkg.python-tornado.4_2_1.rhel7
    - pkg.python-timelib.0_2_4.rhel7
    - pkg.python-urllib3.1_10_2.rhel7
    - pkg.python-yaml.3_11.rhel7
    - pkg.salt.2016_3_7.rhel7
    - pkg.winexe.1_1.rhel7
    - pkg.zeromq.4_1_4.rhel7

{% elif buildcfg.build_release == 'rhel6' %}

    - pkg.babel.0_9_4.rhel6
    - pkg.libsodium.0_4_5.rhel6
    - pkg.libyaml.0_1_3.rhel6
##    - pkg.openpgm.5_1_118.rhel6
    - pkg.pciutils.3_1_10.rhel6
    - pkg.python-backports.1_0.rhel6
    - pkg.python-backports-ssl_match_hostname.3_4_0_2.rhel6
    - pkg.python-chardet.2_2_1.rhel6
    - pkg.python-cherrypy.3_2_2.rhel6
    - pkg.python-crypto.2_6_1.rhel6
    - pkg.python-enum34.1_0.rhel6
    - pkg.python-futures.3_0_3.rhel6
    - pkg.python-importlib.1_0_2.rhel6
    - pkg.python-ioflo.1_3_8.rhel6
    - pkg.python-impacket.0_9_14.rhel6
    - pkg.python-jinja2.2_8_1.rhel6
    - pkg.python-libcloud.0_20_0.rhel6
    - pkg.python-libnacl.1_4_3.rhel6
    - pkg.python-markupsafe.0_11.rhel6
    - pkg.python-msgpack.0_4_6.rhel6
    - pkg.python-ordereddict.1_1.rhel6
    - pkg.python-pip.7_1_0.rhel6
    - pkg.python-pyzmq.14_5_0.rhel6
    - pkg.python-raet.0_6_6.rhel6
    - pkg.python-requests.2_6_0.rhel6
    - pkg.python-six.1_9_0.rhel6
    - pkg.python-timelib.0_2_4.rhel6
    - pkg.python-tornado.4_2_1.rhel6
    - pkg.python-urllib3.1_10_2.rhel6
    - pkg.python-yaml.3_11.rhel6
    - pkg.salt.2016_3_7.rhel6
    - pkg.yum-utils.1_1_30.rhel6
    - pkg.winexe.1_1.rhel6
    - pkg.zeromq.4_0_5.rhel6

{% elif buildcfg.build_release == 'fc24' %}

    - pkg.salt.2016_3_7.fc24

{% endif %}


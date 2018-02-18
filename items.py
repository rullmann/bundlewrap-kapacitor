pkg_dnf = {
    'kapacitor': {
        'needs': ['action:dnf_makecache'],
    },
}

svc_systemd = {
    'kapacitor': {
        'needs': ['pkg_dnf:kapacitor'],
    },
}

files = {
    '/etc/kapacitor/kapacitor.conf': {
        'mode': '0444',
        'content_type': 'mako',
        'needs': ['pkg_dnf:kapacitor'],
        'triggers': ['svc_systemd:kapacitor:restart'],
        'context': {
            'kapacitor': node.metadata.get('kapacitor', {}),
        },
    },
}

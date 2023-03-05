# Conduct regular security assessments
from flask_talisman import Talisman

# Enable Content Security Policy to prevent XSS attacks

csp = {
    'default=src': [
        '\'self\'',
        'https://cdnjs.cloudflare.com',
        'https://fonts.googleapis.com/',
        'https://cdn.jsdelivr.net/',
        'https://stackpath.bootstrapcdn.com/',

    ],
    'style-src': [
    '\'self\'',
    'https://stackpath.bootstrapcdn.com/',
    ],
}

# Enable HTTP strict Transport Security to enforce HTTPs

hsts = {
    'max-age': 31536000,
    'includeSubDomains': True,
}


# Enable X-Frame-Options to prevent clickjacking attacks

frame_options = 'DENY'

# Enable XSS protection in modern browsers
xss_protection = True



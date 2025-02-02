JAZZMIN_SETTINGS = {
    "site_title": "AG-German Institute",
    "site_header": "AG German Management",
    "site_brand": "AG API Portal",
    "site_logo": "img/german_flag.png",
    "login_logo": "img/german_flag.png",
    "login_logo_dark": "img/german_flag.png",
    "site_logo_classes": "img-circle elevation-3",
    "site_icon": "img/german_flag.png",
    "welcome_sign": "Business API Portal 🚀",
    "copyright": "AG German Institute",
    "user_avatar": "avatar",

    "topmenu_links": [
        {"name": "CRM Admin Portal", "url": "https://www.crm-system.germaninstitute.co.ke/admin/", "new_window": True},
        {"name": "School Admin Portal", "url": "https://www.school.germaninstitute.co.ke/login/?next=/", "new_window": True},
        {"model": "auth.User"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "auth": "fas fa-shield-alt",
        "auth.user": "fas fa-user-tie",
        "auth.Group": "fas fa-users-cog",
    },
    "default_icon_parents": "fas fa-folder-open",
    "default_icon_children": "fas fa-solid fa-bug",
    "related_modal_active": True,
    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,

    "order_with_respect_to": ["auth", "communication"],
    "css_variables": {
        "primary": "#1e3a8a",
        "secondary": "#fbbf24",
        "accent": "#dc2626",
        "primary-fg": "#ffffff",
        "secondary-fg": "#ffffff",
        "accent-fg": "#ffffff"
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
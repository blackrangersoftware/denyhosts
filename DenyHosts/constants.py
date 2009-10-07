
import sys

#################################################################################
#        These files will be created relative to prefs WORK_DIR                 #
#################################################################################

SECURE_LOG_OFFSET = "offset"
DENIED_TIMESTAMPS = "denied-timestamps"
#PARSED_DATES = "file_dates"
ABUSIVE_HOSTS = "hosts"

ABUSED_USERS_INVALID = "users-invalid"
ABUSED_USERS_VALID = "users-valid"
ABUSED_USERS_AND_HOSTS = "users-hosts"                              
SUSPICIOUS_LOGINS = "suspicious-logins"   # successful logins AFTER invalid
                                          #   attempts from same host

ALLOWED_HOSTS = "allowed-hosts"
ALLOWED_WARNED_HOSTS = "allowed-warned-hosts"

#################################################################################
#                           Miscellaneous constants                             #
#################################################################################

CONFIG_FILE = "denyhosts.cfg"
TAB_OFFSET = 40
DENY_DELIMITER = "# DenyHosts:"
TIME_SPEC_LOOKUP =  {'s': 1,        # s
                     'm': 60,       # minute
                     'h': 3600,     # hour
                     'd': 86400,    # day
                     'w': 604800,   # week
                     'y': 31536000} # year



plat = sys.platform
if plat.startswith("freebsd"):
    # this has no effect if BLOCK_SERVICE is empty
    BSD_STYLE = " : deny"
else:
    BSD_STYLE = ""

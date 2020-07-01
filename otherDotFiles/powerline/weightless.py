class DefaultColor(object):
    """
    This class should have the default colors for every segment.
    Please test every new segment with this theme first.
    """
    # RESET is not a real color code. It is used as in indicator
    # within the code that any foreground / background color should
    # be cleared
    RESET = -1

    USERNAME_FG = 0 # white
    USERNAME_BG = 214 # weightless grey
    USERNAME_ROOT_BG = 88 # weightless dark red

    HOSTNAME_FG = 214 # weightless orange
    HOSTNAME_BG = 240 # grey

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 33  # weightless dark red
    HOME_FG = 0  # white
    PATH_BG = 0 # 250 medium grey
    PATH_FG = 33  # light grey
    CWD_FG = 15  # 254 nearly-white grey
    SEPARATOR_FG = 160

    READONLY_BG = 88
    READONLY_FG = 254

    SSH_BG = 61 #not in use, orange
    SSH_FG = 0

    REPO_CLEAN_BG = 149  # light green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 160  # /red
    REPO_DIRTY_FG = 15  # white

    JOBS_FG = 99 # replaces 39, light purple
    JOBS_BG = 235

    CMD_PASSED_BG = 235
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 160
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 235  # not in use
    SVN_CHANGES_FG = 112  # dark green

    GIT_AHEAD_BG = 235
    GIT_AHEAD_FG = 15
    GIT_BEHIND_BG = 235
    GIT_BEHIND_FG = 15
    GIT_STAGED_BG = 112
    GIT_STAGED_FG = 15
    GIT_NOTSTAGED_BG = 61
    GIT_NOTSTAGED_FG = 15
    GIT_UNTRACKED_BG = 52
    GIT_UNTRACKED_FG = 15
    GIT_CONFLICTED_BG = 9
    GIT_CONFLICTED_FG = 15

    GIT_STASH_BG = 221
    GIT_STASH_FG = 0

    VIRTUAL_ENV_BG = 112
    VIRTUAL_ENV_FG = 00

    BATTERY_NORMAL_BG = 112
    BATTERY_NORMAL_FG = 0
    BATTERY_LOW_BG = 160
    BATTERY_LOW_FG = 0

    AWS_PROFILE_FG = 45
    AWS_PROFILE_BG = 235

    TIME_FG = 15
    TIME_BG = 235


class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass

# coding=utf-8
from __future__ import print_function, unicode_literals

from bgmi.config import BANGUMI_MOE_URL, SHARE_DMHY_URL

ACTION_ADD = 'add'
ACTION_FETCH = 'fetch'
ACTION_FILTER = 'filter'
ACTION_DELETE = 'downloaded'
ACTION_UPDATE = 'update'
ACTION_CAL = 'cal'
ACTION_CONFIG = 'config'
ACTION_DOWNLOAD = 'download'
ACTION_FOLLOWED = 'followed'
ACTION_LIST = 'list'
ACTION_MARK = 'mark'
ACTION_SEARCH = 'search'
ACTION_SOURCE = 'source'
ACTIONS = (ACTION_ADD, ACTION_DELETE, ACTION_UPDATE, ACTION_CAL,
           ACTION_CONFIG, ACTION_FILTER, ACTION_FETCH, ACTION_DOWNLOAD, ACTION_FOLLOWED,
           ACTION_LIST, ACTION_MARK, ACTION_SEARCH, ACTION_SOURCE)

FILTER_CHOICE_TODAY = 'today'
FILTER_CHOICE_ALL = 'all'
FILTER_CHOICE_FOLLOWED = 'followed'
FILTER_CHOICES = (FILTER_CHOICE_ALL, FILTER_CHOICE_FOLLOWED, FILTER_CHOICE_TODAY)

DOWNLOAD_ACTION_LIST = 'list'
DOWNLOAD_ACTION_MARK = 'mark'
DOWNLOAD_ACTION = (DOWNLOAD_ACTION_LIST, DOWNLOAD_ACTION_MARK)

DOWNLOAD_CHOICE_LIST_ALL = 'all'
DOWNLOAD_CHOICE_LIST_NOT_DOWNLOAD = 'not_downloaded'
DOWNLOAD_CHOICE_LIST_DOWNLOADING = 'downloading'
DOWNLOAD_CHOICE_LIST_DOWNLOADED = 'downloaded'
DOWNLOAD_CHOICE_LIST_DICT = {
    None: DOWNLOAD_CHOICE_LIST_ALL,
    0: DOWNLOAD_CHOICE_LIST_NOT_DOWNLOAD,
    1: DOWNLOAD_CHOICE_LIST_DOWNLOADING,
    2: DOWNLOAD_CHOICE_LIST_DOWNLOADED,
}

DOWNLOAD_CHOICE = (DOWNLOAD_CHOICE_LIST_ALL, DOWNLOAD_CHOICE_LIST_DOWNLOADED,
                   DOWNLOAD_CHOICE_LIST_DOWNLOADING, DOWNLOAD_CHOICE_LIST_NOT_DOWNLOAD)

FOLLOWED_ACTION_LIST = 'list'
FOLLOWED_ACTION_MARK = 'mark'
FOLLOWED_CHOICE = (FOLLOWED_ACTION_LIST, FOLLOWED_ACTION_MARK)
SUPPORT_WEBSITE = [
    {
        'view': '萌番组 https://bangumi.moe/',
        'id': "bangumi_moe",
        'url': BANGUMI_MOE_URL
    },
    {
        'view': '蜜柑计划 https://mikanani.me/',
        'id': 'mikan_project',
        'url': 'https://mikanani.me/'
    },
    {
        'view': '动漫花园 http://share.dmhy.org/',
        'id': 'dmhy',
        'url': SHARE_DMHY_URL
    },
]
STATUS_SUCCESS = 'success'
STATUS_WARNING = 'warning'
STATUS_ERROR = 'error'
STATUS_INFO = 'info'

SPACIAL_APPEND_CHARS = ['Ⅱ', 'Ⅲ', '♪', 'Δ', '×', '☆', 'É', '·', '♭', '★']
SPACIAL_REMOVE_CHARS = []

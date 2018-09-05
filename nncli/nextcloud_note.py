# -*- coding: utf-8 -*-

from requests.exceptions import RequestException, ConnectionError
import time
import datetime
import logging
import requests
import traceback

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson as json

class NextcloudNote(object):
    """ Class for interacting with the NextCloud Notes web service """

    def __init__(self, username, password, host):
        """ object constructor """
        self.username = username
        self.password = password
        self.url = \
            'https://{}/index.php/apps/notes/api/v0.2/notes'. \
            format(host)
        self.status = 'offline'

    def get_note(self, noteid):
        """ method to get a specific note

        Arguments:
            - noteid (string): ID of the note to get

        Returns:
            A tuple `(note, status)`

            - note (dict): note object
            - status (int): 0 on sucesss and -1 otherwise

        """
        # request note
        url = '{}/{}'.format(self.url, str(noteid))
        #logging.debug('REQUEST: ' + self.url+params)
        try:
            res = requests.get(url, auth=(self.username, self.password))
            res.raise_for_status()
            note = res.json()
            self.status = 'online'
        except ConnectionError as e:
            self.status = 'offline, connection error'
            return e, -1
        except RequestException as e:
            # logging.debug('RESPONSE ERROR: ' + str(e))
            return e, -1
        except ValueError as e:
            return e, -1

        # # use UTF-8 encoding
        # note["content"] = note["content"].encode('utf-8')
        # # For early versions of notes, category is not always available
        # if "category" in note:
        #     note["category"] = [t.encode('utf-8') for t in note["category"]]
        #logging.debug('RESPONSE OK: ' + str(note))
        return note, 0

    def update_note(self, note):
        """ function to update a specific note object, if the note
        object does not have a "key" field, a new note is created

        Arguments
            - note (dict): note object to update

        Returns:
            A tuple `(note, status)`

            - note (dict): note object
            - status (int): 0 on sucesss and -1 otherwise

        """
        # Note: all strings in notes stored as type str
        # - use s.encode('utf-8') when bytes type needed

        # determine whether to create a new note or updated an existing one
        if "id" in note:
            # set modification timestamp if not set by client
            if 'modified' not in note:
                note["modified"] = int(time.time())

            url = '{}/{}'.format(self.url, note["id"])
            del note["id"]
        else:
            url = self.url

        #logging.debug('REQUEST: ' + url + ' - ' + str(note))
        try:
            logging.debug('NOTE: ' + str(note))
            if url != self.url:
                res = requests.put(url, auth=(self.username,
                    self.password), json=note)
            else:
                res = requests.post(url, auth=(self.username,
                    self.password), json=note)
            note = res.json()
            res.raise_for_status()
            logging.debug('NOTE (from response): ' + str(res.json()))
            self.status = 'online'
        except ConnectionError as e:
            self.status = 'offline, connection error'
            return e, -1
        except RequestException as e:
            logging.debug('RESPONSE ERROR: ' + str(e))
            logging.debug(traceback.print_exc())
            self.status = 'error updating note, check log'
            return e, -1
        except ValueError as e:
            return e, -1
        #logging.debug('RESPONSE OK: ' + str(note))
        return note, 0

    def get_note_list(self, category=None):
        """ function to get the note list

        The function can be passed optional arguments to limit the
        date range of the list returned and/or limit the list to notes
        containing a certain category. If omitted a list of all notes
        is returned.

        Arguments:
            - category=None category as string: return notes tagged to
              this category

        Returns:
            A tuple `(notes, status)`

            - notes (list): A list of note objects with all properties
              set except `content`.
            - status (int): 0 on sucesss and -1 otherwise

        """
        # initialize data
        status = 0
        note_list = {}

        # get the note index
        params = {'exclude': 'content'}

        # perform initial HTTP request
        try:
            logging.debug('REQUEST: ' + self.url + \
                '?exclude=content')
            res = requests.get(self.url, auth=(self.username, self.password), params=params)
            res.raise_for_status()
            #logging.debug('RESPONSE OK: ' + str(res))
            note_list = res.json()
            self.status = 'online'
        except ConnectionError as e:
            logging.exception('connection error')
            self.status = 'offline, connection error'
            status = -1
        except RequestException as e:
            # if problem with network request/response
            logging.exception('request error')
            status = -1
        except ValueError as e:
            # if invalid json data
            status = -1
            logging.exception('request returned bad JSON data')

        # Can only filter for category at end, once all notes have been
        # retrieved. Below based on simplenote.vim, except we return
        # deleted notes as well
        if category is not None:
            note_list = \
                [n for n in note_list if n["category"] == category]

        return note_list, status

    def delete_note(self, note):
        """ method to permanently delete a note

        Arguments:
            - note_id (string): key of the note to delete

        Returns:
            A tuple `(note, status)`

            - note (dict): an empty dict or an error message
            - status (int): 0 on sucesss and -1 otherwise

        """
        url = '{}/{}'.format(self.url, str(note['id']))

        try:
            logging.debug('REQUEST DELETE: ' + url)
            res = requests.delete(url, auth=(self.username, self.password))
            res.raise_for_status()
            self.status = 'online'
        except ConnectionError as e:
            self.status = 'offline, connection error'
            return e, -1
        except RequestException as e:
            return e, -1
        return {}, 0

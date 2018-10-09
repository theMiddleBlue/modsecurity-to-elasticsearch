# ModSecurity JSON to Elasticsearch
please, read the following post before using it:
[https://medium.com/@themiddleblue/modsecurity-elasticsearch-kibana-40e4f8191e35](https://medium.com/@themiddleblue/modsecurity-elasticsearch-kibana-40e4f8191e35)

### Usage:
```bash
python modsec_parser.py -d <auditlog directory>
```

### Example:
```
$ python modsec_parser.py -d /usr/local/nginx/logs/modsecurity/www.example.com
Parsed /usr/local/nginx/logs/modsecurity/www.example.com/20171114/20171114-1714/20171114-171410-151067605036.512983
Sleeping for a while...
```

### Options:

```
$ python2 modsec_parser.py --help

    usage:  -d  "modsecurity Audity log dir"    -h   "Elasticsearch ip"    -p   "Elasticsearch host"    -s seconds

    -d, --log-directory  Same as your SecAuditLogStorageDir var in modsecurity.conf
    -h, --host           Elasticsearch ip - default 127.0.0.1
    -p, --port           Elasticsearch port - default 9200
    -s, --sleep          Sleeping for n seconds - default 5
    -H, --help           Print this help summary page


```


Run it in background

```
$ python modsec_parser.py -d /usr/local/nginx/logs/modsecurity/www.example.com > /dev/null 2>&1 &
```

### Service:



### Contributors
probably your python skills are better then mine, so all contributions are appreciated :)


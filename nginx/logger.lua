local cjson = require "cjson"
local json = cjson.new()
local log_line = {}

log_line.response = {}
log_line.response.headers = ngx.resp.get_headers()

ngx.var.log_line = json.encode(log_line)
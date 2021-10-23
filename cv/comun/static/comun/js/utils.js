/*jshint esversion: 6 */

function __console(name) {    
    return console[name].bind(console)
}

function fake_dbg() {}

var dbg = __console('log')
var warn = __console('warn')
var err = __console('error')
var assert = __console('assert')
var dir = __console('dir')
var dirx = __console('dirxml')
var trace = __console('trace')

var is_try = function(cond, err_msg) {
    if (cond) return
    throw 'is not try: ' + err_msg
}

function start_safe(fn, param) {
    try {
        //dbg('p_call in')
        var fn_res = fn(param)
        //dbg('p_call out')
        return { is_fail:false, res: fn_res }
    } catch (e) {
        return { is_fail:true, err: e }
    }
}

var qsO = document.querySelector.bind(document)
var qsA = document.querySelectorAll.bind(document)

function __start_finisher(timer_id) {
    return {
        finish: function() {
            clearTimeout(timer_id)
        }
    }
}

function start_every(ms, fn) {
    fn()
    var timer_id = setInterval(fn, ms)
    return __start_finisher(timer_id)
}

function start_after(ms, fn) {
    return __start_finisher(setTimeout(fn, ms))
}

function get_arg(name) {
    let founds = new RegExp('[?&]'+encodeURIComponent(name)+'=([^&]*)').exec(location.search)
    if (founds)
	    return decodeURIComponent(founds[1])
}

function random_int(max, min=0) {
    return min+Math.floor(Math.random()*Math.floor(max-min));
}

function rnd(max, min=0) {
    return random_int(max, min)
}

function random_range(min, max) {
    return random_int(max, min)
}


function get_cookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}

function set_cookie(name, value, options = {}) {
    options = {
        path: '/',
        //...options
    }

    if (options.expires instanceof Date) {
        options.expires = options.expires.toUTCString()
    }

    let updated_cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value)

    for (let option_name in options) {
        updated_cookie += "; " + option_name
        let val = options[option_name]
        
        if (val !== true) {
            updated_cookie += "=" + val
        }
    }

    document.cookie = updated_cookie
}

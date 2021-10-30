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
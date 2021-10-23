import sass
import os


sass.compile(
    dirname=('./quatropack/static/quatropack/styles/sass', './quatropack/static/quatropack/styles'), 
    output_style='compressed')

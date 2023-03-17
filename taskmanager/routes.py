from flask import Flask, render_template
from taskmanager import app, db
from flask_sqlalchemy import SQLAlchemy
from taskmanager.database import Category, Task




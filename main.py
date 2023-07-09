from flask import Flask, jsonify, request
import random
import json

server_port = 3673
app = Flask(__name__)

jokesarray = ["Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
              "I bought some shoes from a drug dealer. I don't know what he laced them with, but I've been tripping "
              "all day.",
              "I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
              "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
              "I'm so good at sleeping. I can do it with my eyes closed.",
              "My boss told me to have a good day.. so I went home.",
              "Why is Peter Pan always flying? He never lands.",
              "Did you hear the one about the guy with the broken hearing aid? Neither did he.",
              "What do you call a fly without wings? A walk.",
              "When my wife told me to stop impersonating a flamingo, I had to put my foot down.",
              "What do you call someone with no nose? Nobody knows.",
              "What time did the man go to the dentist? Tooth hurt-y.",
              "Why can’t you hear a pterodactyl go to the bathroom? The p is silent.",
              "How many optometrists does it take to change a light bulb? 1 or 2? 1... or 2?",
              "I was thinking about moving to Moscow but there is no point Russian into things.",
              "Why does Waldo only wear stripes? Because he doesn't want to be spotted.",
              "Do you know where you can get chicken broth in bulk? The stock market."
              "I used to work for a soft drink can crusher. It was soda pressing."]


@app.route("/")
def index():
    return json.dumps(jokesarray)


@app.route("/jokesarray", methods=['GET'])
def get_numjokes():
    
    numjokes = request.args.get('num', default=1, type=int)
    random_jokes = random.sample(jokesarray, numjokes)
    return jsonify(random_jokes)


if __name__ == '__main__':
    app.run('0.0.0.0', port=server_port)

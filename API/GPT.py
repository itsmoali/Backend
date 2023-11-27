import os
import openai
import json

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

# json_file = "Backend\GPT_API\example.json"

# with open(json_file) as f:
#     data = json.load(f)
data = {
    "course":  "Python",
    "diffuculty" : "beginner",
    "duration" : "20 days",
    "description": [
      {
        "day": 1,
        "topics": [
          {
            "title": "Understanding the Game",
            "subtopics": [
              "Chess History and Cultural Significance",
              "Objective of the Game",
              "Chess as Skill and Strategy"
            ]
          }
        ]
      },
      {
        "day": 2,
        "topics": [
          {
            "title": "Chessboard Basics",
            "subtopics": [
              "Chessboard Layout",
              "Ranks and Files Recap"
            ]
          }
        ]
      },
      {
        "day": 3,
        "topics": [
          {
            "title": "Chess Notation",
            "subtopics": [
              "Algebraic Notation",
              "Reading and Writing Moves",
              "Importance of Recording Games"
            ]
          }
        ]
      },
      {
        "day": 4,
        "topics": [
          {
            "title": "Setting up the Chessboard",
            "subtopics": [
              "Placing Pieces Correctly",
              "Identifying Pieces"
            ]
          }
        ]
      },
      {
        "day": 5,
        "topics": [
          {
            "title": "How Chess Pieces Move",
            "subtopics": [
              "Pawn Movement and Capturing",
              "Movement Rules for Each Piece"
            ]
          }
        ]
      },
      {
        "day": 6,
        "topics": [
          {
            "title": "Special Moves - Castling",
            "subtopics": [
              "Castling as a Defensive Move",
              "When and How to Castle"
            ]
          }
        ]
      },
      {
        "day": 7,
        "topics": [
          {
            "title": "Special Moves - En Passant and Pawn Promotion",
            "subtopics": [
              "En Passant Capture",
              "Pawn Promotion Rules and Strategies"
            ]
          }
        ]
      },
      {
        "day": 8,
        "topics": [
          {
            "title": "Importance of the Center",
            "subtopics": [
              "Significance of Central Control",
              "Centralization of Pieces"
            ]
          }
        ]
      },
      {
        "day": 9,
        "topics": [
          {
            "title": "Pawn Structures",
            "subtopics": [
              "Different Pawn Formations",
              "Common Patterns and Plans"
            ]
          }
        ]
      },
      {
        "day": 10,
        "topics": [
          {
            "title": "Opening Principles",
            "subtopics": [
              "Developing Pieces in the Opening",
              "Common Opening Mistakes"
            ]
          }
        ]
      },
      {
        "day": 11,
        "topics": [
          {
            "title": "Development and Piece Activity",
            "subtopics": [
              "Efficient Piece Development",
              "Exploiting Opponent’s Underdeveloped Pieces"
            ]
          }
        ]
      },
      {
        "day": 12,
        "topics": [
          {
            "title": "Basic Checkmating Patterns",
            "subtopics": [
              "Back Rank Mate",
              "Simple Checkmating Combinations"
            ]
          }
        ]
      },
      {
        "day": 13,
        "topics": [
          {
            "title": "Tactics - Forks and Pins",
            "subtopics": [
              "Understanding Forks",
              "Identifying Pins"
            ]
          }
        ]
      },
      {
        "day": 14,
        "topics": [
          {
            "title": "Tactics - Skewers and Discovered Attacks",
            "subtopics": [
              "Recognizing Skewers",
              "Discovered Attacks and Strategies"
            ]
          }
        ]
      },
      {
        "day": 15,
        "topics": [
          {
            "title": "Open Files and Outposts",
            "subtopics": [
              "Importance of Open Files",
              "Creating Outposts"
            ]
          }
        ]
      },
      {
        "day": 16,
        "topics": [
          {
            "title": "Pawn Breaks",
            "subtopics": [
              "Strategic Use of Pawn Breaks",
              "Recognizing Favorable Moments for Pawn Breaks"
            ]
          }
        ]
      },
      {
        "day": 17,
        "topics": [
          {
            "title": "Initiative and Counterplay",
            "subtopics": [
              "Seizing the Initiative",
              "Creating Counterplay"
            ]
          }
        ]
      },
      {
        "day": 18,
        "topics": [
          {
            "title": "Recognizing Tactical Themes",
            "subtopics": [
              "Expanding Tactical Awareness",
              "Solving Tactical Puzzles"
            ]
          }
        ]
      },
      {
        "day": 19,
        "topics": [
          {
            "title": "Planning and Positional Understanding",
            "subtopics": [
              "Formulating Strategic Plans",
              "Understanding Key Positional Concepts"
            ]
          }
        ]
      },
      {
        "day": 20,
        "topics": [
          {
            "title": "Introduction to Endgames",
            "subtopics": [
              "Transitioning from Middle Game to Endgame",
              "Basic Endgame Principles"
            ]
          }
        ]
      }]}


def create_course(duration, topic, difficulty):
    

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-1106",
        response_format = {"type": "json_object"},
        messages = [
            {"role": "system", "content":"You are a helpful assistant that helps people create courses on various topics. The output should strictly be in JSON. If the output isnot in JSON, the system will not accept it."},
            {"role":"user", "content":"Create me a 20 day course on Chess. I am a beginner so make sure to include the basics."},
            {"role": "system", "content":"Here is your course: " + str(data)},
            {"role": "user", "content":"Create me a "  + duration + "day course on " + topic + ". I am a " + difficulty + " so be sure to construct it according to my proficiency." }
        ],
        max_tokens = 1000,
        temperature = 0.2,
    )
    if response.choices[0].finish_reason == 'stop':
         
         response = response.choices[0].message.content

         return json.loads(response)

    
    elif response.choices[0].finish_reason == 'length':
        return response.choices[0].message.content







#!/usr/bin/python3
"""
Module to fetch and process data from a RESTful API using requests.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints status code,
    and prints the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves id, title,
    and body of each post into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]
        fieldnames = ["id", "title", "body"]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

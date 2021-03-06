#!/usr/bin/python3

import requests
import sys

def AsciiArt():
    print("""
  ────────────────────────────────
  ───────────────██████████───────
  ──────────────████████████──────
  ──────────────██────────██──────
  ──────────────██▄▄▄▄▄▄▄▄▄█──────
  ──────────────██▀███─███▀█──────
  █─────────────▀█────────█▀──────
  ██──────────────────█───────────
  ─█──────────────██──────────────
  █▄────────────████─██──████
  ─▄███████████████──██──██████ ──
  ────█████████████──██──█████████
  ─────────────████──██─█████──███
  ──────────────███──██─█████──███
  ──────────────███─────█████████
  ──────────────██─────████████▀
  ────────────────██████████
  ────────────────██████████
  ─────────────────████████
  ──────────────────██████████▄▄
  ────────────────────█████████▀
  ─────────────────────████──███
  ────────────────────▄████▄──██
  ────────────────────██████───▀
  ────────────────────▀▄▄▄▄▀
  Discord: Junko Yasujiro#5161"""
  )

def request(cep):
  global headers
  r = requests.get(url=cep, headers=headers)
  return r.text

if __name__=='__main__':
  AsciiArt()

  headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Accept': 'application/json'
  }

  try:
    r = request("http://cep.la/{}".format(sys.argv[1]))
    print(r)
  except Exception as error:
    print("Ocorreu um erro: ", error)
  finally:
    print("\nObrigado por usar a ferramenta!")

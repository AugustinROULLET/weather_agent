"""Main entry point"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from agents import Runner
from agent import style_agent
from config import config

async def main():
    """Main application loop"""
    
    print("\n" + "="*50)
    print("👔 UNIVERSAL STYLE COACH 👔")
    print("="*50)
    
    print("\n✨ I'll advise you on what to wear based on the weather!")
    
    print("\n🔴 Type 'quit' to exit\n")
    
    
    while True:
        user_input = input("\nAsk your question: ").strip()
        
        if user_input.lower() in config.EXIT_COMMANDS:
            print("\nSee you soon!")
            break
        
        if not user_input:
            continue
        
        try:
            result = await Runner.run(style_agent, user_input)
            print(f"\n{result.final_output}")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Can you rephrase or try another city?")

if __name__ == "__main__":
    asyncio.run(main())
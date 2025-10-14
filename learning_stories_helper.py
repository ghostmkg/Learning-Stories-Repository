#!/usr/bin/env python3
"""
🎓 Learning Stories Code Helper
A simple tool to help beginners learn coding concepts through interactive examples.

This tool demonstrates:
- Basic Python concepts
- File I/O operations
- String manipulation
- Simple algorithms
- Error handling

Author: AI Assistant Helper
Date: December 2024
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class LearningStoriesHelper:
    """A helper class for learning coding concepts through stories."""
    
    def __init__(self):
        self.stories_data = []
        self.load_stories()
    
    def load_stories(self):
        """Load stories from the stories directory."""
        stories_dir = "stories"
        if os.path.exists(stories_dir):
            for filename in os.listdir(stories_dir):
                if filename.endswith('.md'):
                    story_path = os.path.join(stories_dir, filename)
                    try:
                        with open(story_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            self.stories_data.append({
                                'filename': filename,
                                'content': content,
                                'word_count': len(content.split()),
                                'char_count': len(content)
                            })
                    except Exception as e:
                        print(f"Error reading {filename}: {e}")
    
    def analyze_stories(self) -> Dict[str, Any]:
        """Analyze the stories and provide statistics."""
        if not self.stories_data:
            return {"error": "No stories found"}
        
        total_stories = len(self.stories_data)
        total_words = sum(story['word_count'] for story in self.stories_data)
        total_chars = sum(story['char_count'] for story in self.stories_data)
        
        # Find the longest and shortest stories
        longest_story = max(self.stories_data, key=lambda x: x['word_count'])
        shortest_story = min(self.stories_data, key=lambda x: x['word_count'])
        
        return {
            "total_stories": total_stories,
            "total_words": total_words,
            "total_characters": total_chars,
            "average_words_per_story": total_words // total_stories if total_stories > 0 else 0,
            "longest_story": {
                "filename": longest_story['filename'],
                "word_count": longest_story['word_count']
            },
            "shortest_story": {
                "filename": shortest_story['filename'],
                "word_count": shortest_story['word_count']
            }
        }
    
    def search_stories(self, keyword: str) -> List[Dict[str, Any]]:
        """Search for stories containing a specific keyword."""
        results = []
        keyword_lower = keyword.lower()
        
        for story in self.stories_data:
            if keyword_lower in story['content'].lower():
                # Count occurrences
                occurrences = story['content'].lower().count(keyword_lower)
                results.append({
                    'filename': story['filename'],
                    'occurrences': occurrences,
                    'preview': self._get_preview(story['content'], keyword)
                })
        
        return sorted(results, key=lambda x: x['occurrences'], reverse=True)
    
    def _get_preview(self, content: str, keyword: str, length: int = 100) -> str:
        """Get a preview of the content around the keyword."""
        keyword_lower = keyword.lower()
        content_lower = content.lower()
        
        # Find the first occurrence
        index = content_lower.find(keyword_lower)
        if index == -1:
            return content[:length] + "..."
        
        # Get context around the keyword
        start = max(0, index - length // 2)
        end = min(len(content), index + length // 2)
        
        preview = content[start:end]
        if start > 0:
            preview = "..." + preview
        if end < len(content):
            preview = preview + "..."
        
        return preview
    
    def generate_learning_report(self) -> str:
        """Generate a learning report about the stories."""
        analysis = self.analyze_stories()
        
        report = f"""
# 📊 Learning Stories Analysis Report
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📈 Statistics
- **Total Stories**: {analysis.get('total_stories', 0)}
- **Total Words**: {analysis.get('total_words', 0):,}
- **Total Characters**: {analysis.get('total_characters', 0):,}
- **Average Words per Story**: {analysis.get('average_words_per_story', 0)}

## 📚 Story Highlights
- **Longest Story**: {analysis.get('longest_story', {}).get('filename', 'N/A')} 
  ({analysis.get('longest_story', {}).get('word_count', 0)} words)
- **Shortest Story**: {analysis.get('shortest_story', {}).get('filename', 'N/A')} 
  ({analysis.get('shortest_story', {}).get('word_count', 0)} words)

## 🎯 Learning Insights
This repository contains {analysis.get('total_stories', 0)} inspiring stories from developers 
around the world, sharing their journey in open source development. Each story is a 
valuable learning resource for beginners and experienced developers alike.

---
*Report generated by Learning Stories Helper Tool*
        """
        
        return report.strip()

def main():
    """Main function to demonstrate the tool."""
    print("🎓 Welcome to Learning Stories Helper!")
    print("=" * 50)
    
    helper = LearningStoriesHelper()
    
    # Generate and display analysis
    print("\n📊 Analyzing stories...")
    analysis = helper.analyze_stories()
    
    if "error" in analysis:
        print(f"❌ {analysis['error']}")
        return
    
    print(f"✅ Found {analysis['total_stories']} stories")
    print(f"📝 Total words: {analysis['total_words']:,}")
    print(f"📏 Average words per story: {analysis['average_words_per_story']}")
    
    # Interactive search
    print("\n🔍 Interactive Search")
    print("Enter keywords to search in stories (or 'quit' to exit):")
    
    while True:
        try:
            keyword = input("\nSearch for: ").strip()
            if keyword.lower() in ['quit', 'exit', 'q']:
                break
            
            if not keyword:
                continue
            
            results = helper.search_stories(keyword)
            
            if not results:
                print(f"❌ No stories found containing '{keyword}'")
            else:
                print(f"\n✅ Found {len(results)} story(ies) containing '{keyword}':")
                for i, result in enumerate(results[:5], 1):  # Show top 5 results
                    print(f"\n{i}. {result['filename']} ({result['occurrences']} occurrence(s))")
                    print(f"   Preview: {result['preview']}")
                
                if len(results) > 5:
                    print(f"\n... and {len(results) - 5} more results")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Generate report
    print("\n📋 Generating learning report...")
    report = helper.generate_learning_report()
    
    # Save report to file
    report_filename = f"learning_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    try:
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Report saved as: {report_filename}")
    except Exception as e:
        print(f"❌ Error saving report: {e}")
        print("\n📋 Report Preview:")
        print(report)

if __name__ == "__main__":
    main()

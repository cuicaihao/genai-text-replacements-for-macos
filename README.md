# GenAI Prompt Engineering Text Substitutions for macOS

This repository contains a comprehensive collection of text substitutions designed for GenAI prompt engineering, specifically tailored for tech professionals working in AI/ML engineering, Agile environments, and DevOps practices.

## Overview

This repository provides a `Text Substitutions.plist` file containing 45 prompt engineering shortcuts for GenAI tools like ChatGPT, Claude, and Copilot. These shortcuts are designed to streamline tasks for tech professionals, covering areas such as professional communication, Agile workflows, DevOps, and technical leadership.

## Quick Reference Guide

### General Office & Communication (21 shortcuts)

- **`zzed`** - Professional text editing and refinement
- **`zzedbiz`** - Business writing refinement for clarity, conciseness, and professional tone
- **`zzedacad`** - Academic peer review for clarity, logical flow, and formal tone
- **`zzeddual`** - Dual output: minimal edits and fully optimized version for professional audience
- **`zzedcasual`** - Casual blog editing for readability and personal voice
- **`zzsum`** - Content summarization with key topics
- **`zzemail`** - Professional email composition
- **`zzagenda`** - Meeting agenda creation
- **`zzsimplify`** - Technical concept simplification
- **`zzplan`** - Project planning and management
- **`zzanalyze`** - Business data analysis
- **`zzslides`** - Presentation outline creation
- **`zznotes`** - Meeting notes organization
- **`zzqa`** - Quality assurance review
- **`zzbrainstorm`** - Creative ideation
- **`zzdiplomacy`** - Diplomatic communication
- **`zzresearch`** - Research compilation
- **`zztasks`** - Task breakdown and organization
- **`zzformat`** - Content formatting and structure
- **`zztranslate`** - Professional translation
- **`zzproof`** - Proofreading and editing
- **`zzfollow`** - Follow-up message creation
- **`zztutorial`** - Tutorial and guide development
- **`zzservice`** - Customer service responses
- **`zzreport`** - Executive summary and report writing

### Agile & JIRA Workflow (5 shortcuts)

- **`zzstory`** - User story breakdown with technical tasks and story points
- **`zzjira`** - JIRA ticket creation with acceptance criteria
- **`zzsprint`** - Sprint planning with capacity management for DE/DS teams
- **`zzretro`** - Technical retrospective analysis and improvements
- **`zzbacklog`** - Feature prioritization based on business value and complexity

### CI/CD & DevOps (5 shortcuts)

- **`zzcicd`** - ML model deployment pipeline documentation
- **`zzmlops`** - MLOps monitoring and alerting strategies
- **`zzgit`** - Git workflow and branching strategy for ML projects
- **`zzinfra`** - Containerization and Kubernetes orchestration
- **`zztest`** - ML testing strategies (unit, integration, model validation)

### Technical Leadership (5 shortcuts)

- **`zzreview`** - ML code review checklists
- **`zzarch`** - ML system architecture design
- **`zzpipeline`** - Data pipeline specifications for ML
- **`zzrisk`** - Risk assessment for AI/ML projects
- **`zzxfunc`** - Cross-functional team communication (DE/DS/Engineering)

### System & Performance (5 shortcuts)

- **`zzapi`** - ML service API documentation
- **`zzperf`** - ML system performance optimization
- **`zzsec`** - AI/ML security assessment
- **`zzincident`** - ML system incident post-mortems
- **`zzstake`** - Technical-to-business communication for stakeholders

## How to Import Text Substitutions into macOS

### Method 1: Using System Preferences (Recommended)

1. **Open System Preferences**
   - Click the Apple menu → System Preferences
   - Or use Spotlight (⌘ + Space) and type "System Preferences"

2. **Navigate to Keyboard Settings**
   - Click on "Keyboard"
   - Select the "Text" tab

3. **Import the plist file**
   - Click the "+" button at the bottom left
   - Navigate to the `Text Substitutions.plist` file location
   - Select the file and click "Open"
   - All shortcuts will be automatically imported

### Method 2: Manual Import via Terminal

```bash
cd <your-folder-containing-plist>
cp "Text Substitutions.plist" ~/Library/KeyBindings/
# Restart any applications for changes to take effect
```

### Method 3: Drag and Drop

1. Open Finder and navigate to the `Text Substitutions.plist` file
2. Open System Preferences → Keyboard → Text
3. Drag the plist file directly into the text replacements list
4. macOS will automatically parse and add all entries

## Verification Steps

After importing, verify the installation:

1. **Check System Preferences**
   - Go to Keyboard → Text
   - You should see all 45 shortcuts listed
   - Each should show the shortcut (e.g., `zzed`) and its corresponding phrase

2. **Test a shortcut**
   - Open any text application (Notes, TextEdit, etc.)
   - Type one of the shortcuts (e.g., `zzed`)
   - Press Space or Tab
   - The full prompt should appear

## Usage Tips

### Best Practices

- **Consistent Prefix**: All shortcuts use the `zz` prefix to avoid conflicts with common words
- **Memorable Names**: Shortcuts are designed to be intuitive and easy to remember
- **Context Switching**: Use different shortcuts for different types of tasks to maintain AI context
- **Customization**: Feel free to modify phrases to match your specific workflow needs

### Example Workflow

1. **Planning Phase**: Use `zzplan`, `zzstory`, `zzsprint`
2. **Development Phase**: Use `zzarch`, `zzpipeline`, `zzreview`
3. **Deployment Phase**: Use `zzcicd`, `zzmlops`, `zztest`
4. **Communication**: Use `zzemail`, `zzstake`, `zznotes`
5. **Documentation**: Use `zzapi`, `zztutorial`, `zzreport`

### Customization

To add your own shortcuts or modify existing ones:

1. Edit the `Text Substitutions.plist` file directly
2. Follow the same XML structure for new entries
3. Re-import the file using the methods above
4. Restart applications to see changes

## Troubleshooting

### Common Issues

- **Shortcuts not working**: Restart the application or log out/in
- **Duplicates**: Remove old entries before importing new ones
- **Conflicts**: Check for existing shortcuts that might conflict
- **Sync issues**: Text replacements sync via iCloud, ensure it's enabled

### Reset Text Replacements

To start fresh:

```bash
# Remove all current text replacements
defaults delete -g NSUserReplacementItems
killall SystemUIServer
```

## Technical Specifications

- **File Format**: Apple Property List (plist) XML format
- **Compatibility**: macOS 10.12+ (Sierra and later)
- **Sync**: Automatically syncs across devices via iCloud
- **Backup**: Located at `~/Library/Preferences/.GlobalPreferences.plist`

## Contributing

To suggest new shortcuts or improvements:

1. Fork this repository
2. Add new entries following the existing pattern
3. Test thoroughly across different applications
4. Submit a pull request with clear descriptions

## License

This project is open source. Feel free to modify and distribute according to your needs.

---

- **Version**: 1.2
- **Last Updated**: September 26, 2025
- **Total Shortcuts**: 45

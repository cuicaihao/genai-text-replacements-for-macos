# GenAI Text Replacements for macOS

[简体中文](README.zh-CN.md)

![GenAI Text Replacements for macOS](assets/feature-image.png)

This repository contains a comprehensive collection of text substitutions designed for GenAI prompt engineering, specifically tailored for tech professionals working in AI/ML engineering, Agile environments, and DevOps practices.

## Overview

This repository provides a `Text Substitutions.plist` file containing 50 prompt engineering shortcuts for GenAI tools like ChatGPT, Claude, and Copilot. These shortcuts streamline tasks for tech professionals, covering areas such as professional communication, Agile workflows, DevOps, and technical leadership.

### Version 2.0 Migration

Version 2.0 uses memorable shortcuts with a consistent `zz` prefix. Common actions use familiar words, such as `zzemail`, `zzreply`, and `zzplan`. Related review shortcuts use distinct names: `zzpaper` for academic manuscript reviews, `zzcode` for machine learning code reviews, and `zztech` for production-readiness reviews. If you previously imported an older version, export a backup and remove the old entries before importing the new plist. macOS does not automatically remove shortcuts from an earlier import.

## Quick Reference Guide

### General Office & Communication (28 shortcuts)

- **`zzed`** - Professional text editing and refinement
- **`zzrw`** - Rewrite text in concise, balanced, and forward-looking styles
- **`zzbiz`** - Business writing refinement for clarity and professional tone
- **`zzacad`** - Academic writing refinement with technical terminology preserved
- **`zzpaper`** - Structured academic manuscript review and recommendations
- **`zzdual`** - Minimal edit and optimized rewrite versions
- **`zzcasual`** - Casual writing refinement with the author's voice preserved
- **`zzsum`** - Stakeholder summary with key topics and recommendations
- **`zzemail`** - New professional email composition
- **`zzreply`** - Reply to an email, Slack message, or Google Chat message
- **`zzagenda`** - Meeting agenda creation
- **`zzsimplify`** - Technical concept simplification
- **`zzplan`** - General project planning without an assumed Agile workflow
- **`zzanalyze`** - Business data and context analysis
- **`zzslides`** - Presentation outline creation
- **`zznotes`** - Meeting notes organization
- **`zzqa`** - Quality assurance review
- **`zzbrainstorm`** - Creative ideation
- **`zzdiplomacy`** - Diplomatic communication
- **`zzresearch`** - Research compilation with source links
- **`zztasks`** - Task breakdown and organization
- **`zzformat`** - Content formatting and structure
- **`zztranslate`** - Professional translation
- **`zzproof`** - Proofreading without unnecessary rewriting
- **`zzfollow`** - Follow-up message creation
- **`zztutorial`** - Tutorial and guide development
- **`zzservice`** - Customer service responses
- **`zzreport`** - Executive summary and report writing

### Agile & Jira Workflow (6 shortcuts)

- **`zzstory`** - User story breakdown with technical tasks and story point estimates
- **`zzjira`** - Jira ticket creation with acceptance criteria
- **`zzpm`** - Project management and Agile delivery planning
- **`zzsprint`** - Sprint planning with capacity management for DE/DS teams
- **`zzretro`** - Technical retrospective analysis and improvements
- **`zzbacklog`** - Feature prioritization based on business value and complexity

### CI/CD & DevOps (5 shortcuts)

- **`zzcicd`** - ML model deployment pipeline documentation
- **`zzmlops`** - MLOps monitoring and alerting strategies
- **`zzgit`** - Git workflow and branching strategy for ML projects
- **`zzinfra`** - Infrastructure strategy for ML workloads
- **`zztest`** - ML testing strategies (unit, integration, model validation)

### Technical Leadership (6 shortcuts)

- **`zzcode`** - ML code review with prioritized findings
- **`zztech`** - Production-readiness review for AI/ML systems
- **`zzarch`** - ML system architecture design
- **`zzpipeline`** - Data pipeline specifications for ML
- **`zzrisk`** - Risk assessment for AI/ML projects
- **`zzxfunc`** - Cross-functional team communication (DE/DS/Engineering)

### System & Performance (5 shortcuts)

- **`zzapi`** - ML service API documentation
- **`zzperf`** - ML system performance optimization
- **`zzsec`** - AI/ML security assessment
- **`zzincident`** - ML system post-incident reviews
- **`zzstake`** - Technical-to-business communication for stakeholders

## How to Import Text Substitutions into macOS

> **Important:** Importing this plist adds text replacements to your existing macOS list. It is not a full replacement or reset process. Apple does not document how imports resolve shortcuts that already exist, so duplicate or conflicting shortcuts may require manual cleanup. Before importing, export a backup of your current text replacements. After importing, review the list before relying on the new shortcuts.

Follow Apple's supported drag-and-drop import process:

1. Open **System Settings** on your Mac.
2. Select **Keyboard** in the sidebar.
3. Click **Text Replacements**.
4. In Finder, locate `Text Substitutions.plist`.
5. Drag the plist file into the **Text Replacements** window.
6. Click **Done**.

To export a backup, select your current replacements in the **Text Replacements** window and drag them to Finder. macOS creates a plist backup file that you can re-import if needed.

## Verification Steps

After importing, verify the installation:

1. **Check System Settings**
   - Go to **Keyboard** → **Text Replacements**
   - You should see all 50 shortcuts listed
   - Each should show the shortcut (e.g., `zzed`) and its corresponding phrase

2. **Test a shortcut**
   - Open a compatible text application, such as Notes or TextEdit
   - Type one of the shortcuts (e.g., `zzed`)
   - Press Space or Tab
   - The full prompt should appear

Text replacements are not available in every app. If a shortcut works in Notes or TextEdit but not in another app, check whether that app supports macOS text replacements.

## Usage Tips

### Best Practices

- **Consistent Prefix**: All shortcuts use the `zz` prefix to avoid conflicts with common words
- **Memorable Names**: Shortcuts are designed to be intuitive and easy to remember
- **Context Switching**: Use different shortcuts for different types of tasks to maintain AI context
- **Language Matching**: Prompts reply in the same language as your input unless you request another language. `zztranslate` uses the requested target language
- **Customization**: Feel free to modify phrases to match your specific workflow needs

### Example Workflow

1. **Planning Phase**: Use `zzplan`, `zzstory`, `zzsprint`
2. **Development Phase**: Use `zzarch`, `zzpipeline`, `zzcode`
3. **Deployment Phase**: Use `zzcicd`, `zzmlops`, `zztest`
4. **Communication**: Use `zzemail`, `zzstake`, `zznotes`
5. **Documentation**: Use `zzapi`, `zztutorial`, `zzreport`

### Customization

To add your own shortcuts or modify existing ones:

1. Edit the `Text Substitutions.plist` file directly
2. Follow the same XML structure for new entries
3. Re-import the file using the drag-and-drop method above
4. Restart applications to see changes

## Troubleshooting

### Common Issues

- **Shortcuts not working**: Test the shortcut in Notes or TextEdit, then restart the affected application if needed
- **Duplicates**: Remove old entries before importing new ones
- **Conflicts**: Check for existing shortcuts that might conflict
- **Sync issues**: To sync replacements across Apple devices, enable iCloud Drive and sign in with the same Apple Account on each device

## Technical Specifications

- **File Format**: Apple Property List (plist) XML format
- **Import**: Drag the plist file into **System Settings** → **Keyboard** → **Text Replacements**
- **Sync**: Uses iCloud Drive when devices share the same Apple Account
- **Backup**: Export selected replacements by dragging them from the **Text Replacements** window to Finder

## License

This project is open source. Feel free to modify and distribute according to your needs.

---

- **Version**: 2.0
- **Last Updated**: May 31, 2026
- **Total Shortcuts**: 50

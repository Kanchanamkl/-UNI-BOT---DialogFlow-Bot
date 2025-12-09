# Dialogflow Intents Configuration for Course Resources

## Intent 1: Resources.Query
**Training Phrases:**
- Show me lecture notes for [course_name] week [week_number]
- I need materials for [course_name]
- Get me resources for week [week_number] of [course_name]
- Lecture notes for [course_name]
- Show [course_name] materials
- Week [week_number] [course_name] notes
- I want to see lecture notes
- Show me course materials
- Give me study materials

**Parameters:**
- `course_name` (type: @sys.any, not required)
- `week_number` (type: @sys.number, not required)

**Action:** `query.resources`

**Fulfillment:** Enable webhook

---

## Intent 2: Resources.ProvideCourse
**Training Phrases:**
- [course_name]
- I'm studying [course_name]
- It's [course_name]
- The course is [course_name]

**Parameters:**
- `course_name` (type: @sys.any, required)

**Action:** `provide.course`

**Contexts:**
- Input: `awaiting-course`

**Fulfillment:** Enable webhook

---

## Intent 3: Resources.ProvideWeek
**Training Phrases:**
- Week [week_number]
- [week_number]
- I need week [week_number]
- Show me all weeks
- All weeks

**Parameters:**
- `week_number` (type: @sys.number, not required)

**Action:** `provide.week`

**Contexts:**
- Input: `awaiting-week`

**Fulfillment:** Enable webhook

---

## Custom Entities (Optional)

### @course_name
**Values:**
- Distributed and Cloud System Programming (synonyms: DCSP, distributed, cloud)
- Databases (synonyms: DB, database)
- Digital Forensics (synonyms: DF, forensics)

---

## Example Conversations

**Conversation 1:**
- User: "Show me lecture notes for Databases week 3"
- Bot: [Shows week 3 Database resources with links]

**Conversation 2:**
- User: "I need lecture materials"
- Bot: "Which course are you looking for? • Distributed and Cloud System Programming • Databases • Digital Forensics"
- User: "Databases"
- Bot: "Which week's materials do you need? Available: Week 1, Week 2, ..."
- User: "Week 3"
- Bot: [Shows week 3 resources]

**Conversation 3:**
- User: "Show Digital Forensics materials"
- Bot: "Which week? Available: Week 1, Week 2, ... Or say 'all weeks'"
- User: "All weeks"
- Bot: [Shows all weeks' resources]

# Challenge 1: Soccer Analytics Web Page Creation

**Difficulty: ⭐⭐☆☆☆**

## Challenge Overview

In this challenge, you'll create a static HTML/CSS web page that will serve as a template for displaying soccer analytics data. This will be the foundation for your interactive dashboard in the capstone project.

## Learning Objectives

- Understand HTML document structure and semantic elements
- Apply CSS styling for responsive design
- Create structured layouts for data presentation
- Design user interfaces for sports analytics

## Real-World Context

NCAA soccer programs use analytics dashboards to visualize player and team performance metrics. Coaches and analysts review these dashboards to inform training and game strategies. Your static page will serve as the foundation for an interactive dashboard that could help Division II soccer programs make data-driven decisions.

## Challenge Details

### The Task

Create a static web page using HTML and CSS that:
1. Displays a header with navigation
2. Shows player statistics in a table or card format
3. Presents team performance metrics
4. Includes a form for filtering data
5. Contains placeholders for data visualizations
6. Has a responsive footer section

### HTML Structure Diagram

```
<!DOCTYPE html>
<html>
  <head>
    <!-- Meta info, title, CSS links -->
  </head>
  <body>
    <header>
      <!-- Logo, title, navigation -->
    </header>
    
    <main>
      <section class="dashboard-summary">
        <!-- Overview statistics -->
      </section>
      
      <section class="player-statistics">
        <!-- Player data table/cards -->
      </section>
      
      <section class="team-statistics">
        <!-- Team performance metrics -->
      </section>
      
      <section class="data-filters">
        <!-- Filter form -->
      </section>
      
      <section class="data-visualization">
        <!-- Chart/graph placeholders -->
      </section>
    </main>
    
    <footer>
      <!-- Footer information -->
    </footer>
  </body>
</html>
```

### CSS Approach

Your CSS should:
1. Use a mobile-first responsive design
2. Implement a consistent color scheme
3. Create readable table or card layouts
4. Handle different screen sizes with media queries
5. Use CSS variables for maintainability

## Tips and Hints

### Semantic HTML

Use semantic HTML elements to give structure and meaning to your page:
- `<header>` for the page header
- `<nav>` for navigation menus
- `<main>` for the main content
- `<section>` for distinct page sections
- `<article>` for contained components
- `<table>` for tabular data
- `<form>` for input forms
- `<footer>` for the page footer

### CSS Organization

Consider organizing your CSS in this order:
1. CSS variables and resets
2. Global styles
3. Component-specific styles
4. Media queries for responsive design

### Responsive Design Pattern

```css
/* Mobile styles (base) */
.container {
  display: flex;
  flex-direction: column;
}

/* Tablet styles */
@media (min-width: 768px) {
  .container {
    flex-direction: row;
    flex-wrap: wrap;
  }
  
  .card {
    width: 45%;
  }
}

/* Desktop styles */
@media (min-width: 1024px) {
  .card {
    width: 30%;
  }
}
```

### Player Card Example

```html
<div class="player-card">
  <div class="player-header">
    <h3>John Smith</h3>
    <span class="position">Forward</span>
  </div>
  <div class="player-stats">
    <div class="stat">
      <span class="stat-value">10</span>
      <span class="stat-label">Goals</span>
    </div>
    <div class="stat">
      <span class="stat-value">5</span>
      <span class="stat-label">Assists</span>
    </div>
    <!-- More stats -->
  </div>
</div>
```

## Testing Your Solution

Your solution should:
1. Display correctly on mobile, tablet, and desktop screens
2. Have a clean, readable layout for data presentation
3. Include all required sections (header, player stats, team stats, filter form, visualization placeholders, footer)
4. Use semantic HTML elements appropriately
5. Have consistent styling with CSS

## Application to Capstone

In your capstone project, you will convert this static page into a dynamic dashboard that displays real NCAA soccer data. The HTML structure and CSS styling you create now will serve as the foundation for your interactive application, so focus on creating a clean, maintainable design.

## Resources

- [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [CSS Tricks - A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Tricks - A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Responsive Web Design Basics](https://web.dev/responsive-web-design-basics/)
- [Google Fonts](https://fonts.google.com/) for typography
- [Color Hunt](https://colorhunt.co/) for color scheme inspiration
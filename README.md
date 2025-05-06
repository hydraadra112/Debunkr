# **Debunkr**

## **Description**
A Filipino fake news classifier, created using Python machine learning libraries and SvelteKit with LIME.  
This is a final project for our **CCS 249 - Natural Language Processing** course.  

## **Overview**
**Debunkr** is designed to identify and classify fake news in the Filipino context.  
It leverages machine learning algorithms in Python for back-end processing and SvelteKit for a modern, user-friendly interface.  
The project also incorporates **LIME (Local Interpretable Model-agnostic Explanations)** to make the classification process more transparent and understandable.  

## **Setup**
To properly set up this project, follow the setup instructions for both the frontend and backend components.  

### **Frontend Setup**
1. Navigate to the `./frontend/` directory.  
2. Start the development server:  
   ```bash
   cd ./frontend  
   npm run dev -- --open  
   cd ..  # Return to the root directory

# not recommended to turn on if you're
# doing only front-end
> cd .\backend
> uvicorn main:app --reload --port 8000
```
By following these instructions, we ensure the activation of frontend and backend, enabling them to work together.

## Creators BSCS 3-A AI
- [John Manuel Carado](https://github.com/hydraadra112)
- [Cherilyn Marie Deocampo](https://github.com/chiichann)
- [Mark Andrei Encanto](https://github.com/Markndrei)
- [Chariz Dianne Falco](https://github.com/chariz1101)
- [Jephone Israel Jireh S. Torre](https://github.com/JephoneTorre)
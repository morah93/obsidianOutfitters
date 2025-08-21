Obsidian Outfitters – E-commerce Store

An e-commerce platform I built for my startup clothing brand using Next.js, Tailwind CSS, FastAPI, Stripe, and Printify.
It powers a live storefront where customers can browse products, customize items, and place secure orders — with Printify handling fulfillment.

🚀 Features

Beautiful UI/UX – Responsive, mobile-first design with Tailwind

Product Catalog – Synced automatically from Printify API

Product Pages – Variant selection, dynamic pricing, high-res images

Shopping Cart – Add, update, and remove items (persisted locally)

Secure Checkout – Stripe Checkout with Apple/Google Pay support

Order Handling – Stripe webhooks trigger Printify order creation

Shipping & Status – Basic shipping rates + live order tracking page

AI Chatbot (MVP) – Answers FAQs, hands off to email when needed

SEO & Analytics – Meta tags, sitemap, OpenGraph previews

🛠️ Tech Stack
Frontend

Next.js
 (React Framework)

Tailwind CSS
 for styling

Vercel
 for deployment

Backend

FastAPI
 (Python)

Stripe
 API for payments

Printify API
 for POD fulfillment

Render
 (or Fly.io/Heroku) for deployment

📸 Screenshots
Homepage	Product Page	Checkout

	
	
🔗 Live Demo

👉 mybrand.com
 (replace with your domain)

⚡ How It Works

Catalog Sync – Backend pulls products/variants from Printify → cached in DB

Browse & Cart – Customers browse catalog, add items to cart

Checkout – Stripe Checkout session is created server-side

Payment Success – Stripe webhook triggers → backend creates Printify order

Order Updates – Printify webhook updates order status in app

📂 Project Structure
clothing-site/
├── frontend/    # Next.js + Tailwind app
└── backend/     # FastAPI API (Stripe + Printify webhooks)

💻 Running Locally

Frontend

cd frontend
npm install
npm run dev


Backend

cd backend
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload

🎯 My Role

Designed wireframes, brand palette, and responsive UI

Implemented full-stack e-commerce flow (React + FastAPI)

Integrated Stripe & Printify APIs

Deployed production site + set up CI/CD

📌 Roadmap

 Customer accounts & order history

 Discount codes & promotions

 AI chatbot improvements (fine-tuned Q&A)

 Admin dashboard for sales/analytics

📄 License

MIT License — free to use for learning/inspiration.



import sqlite3

books=[
        {
            "id": "1098127463",
            "title": "Security as Code",
            "subtitle": "DevSecOps Patterns with AWS",
            "authors": "BK Sarthak Das, Virginia Chu",
            "image": "https://www.dbooks.org/img/books/1098127463s.jpg",
            "url": "https://www.dbooks.org/security-as-code-1098127463/"
        },
        {
            "id": "164200233X",
            "title": "ASP.NET Core 6 Succinctly",
            "subtitle": "",
            "authors": "Dirk Strauss",
            "image": "https://www.dbooks.org/img/books/164200233Xs.jpg",
            "url": "https://www.dbooks.org/aspnet-core-6-succinctly-164200233x/"
        },
        {
            "id": "199013209X",
            "title": "Engineering Systems Dynamics, Modelling, Simulation, and Design",
            "subtitle": "Lagrangian and Bond Graph Methods",
            "authors": "Mehrzad Tabatabaian",
            "image": "https://www.dbooks.org/img/books/199013209Xs.jpg",
            "url": "https://www.dbooks.org/engineering-systems-dynamics-modelling-simulation-and-design-199013209x/"
        },
        {
            "id": "5709901124",
            "title": "Build a Raspberry Pi Media Player",
            "subtitle": "Power up your TV and music system",
            "authors": "PJ Evans",
            "image": "https://www.dbooks.org/img/books/5709901124s.jpg",
            "url": "https://www.dbooks.org/build-a-raspberry-pi-media-player-5709901124/"
        },
        {
            "id": "191204742X",
            "title": "The Official Raspberry Pi Handbook 2023",
            "subtitle": "",
            "authors": "David Crookes, PJ Evans, Rosie Hattersley, Phil King, Nicola King, KG Orphanides, Nik Rawlinson, Mark Vanstone",
            "image": "https://www.dbooks.org/img/books/191204742Xs.jpg",
            "url": "https://www.dbooks.org/the-official-raspberry-pi-handbook-2023-191204742x/"
        },
        {
            "id": "5685804586",
            "title": "Pay for Play",
            "subtitle": "How the Music Industry Works, Where the Money Goes, and Why",
            "authors": "Larry Wayte",
            "image": "https://www.dbooks.org/img/books/5685804586s.jpg",
            "url": "https://www.dbooks.org/pay-for-play-5685804586/"
        },
        {
            "id": "1642002275",
            "title": "Azure Bot Service Succinctly",
            "subtitle": "",
            "authors": "Ed Freitas",
            "image": "https://www.dbooks.org/img/books/1642002275s.jpg",
            "url": "https://www.dbooks.org/azure-bot-service-succinctly-1642002275/"
        },
        {
            "id": "1607826593",
            "title": "Introductory Algebra",
            "subtitle": "",
            "authors": "Anne Gloag, Andrew Gloag, Melissa Kramer",
            "image": "https://www.dbooks.org/img/books/1607826593s.jpg",
            "url": "https://www.dbooks.org/introductory-algebra-1607826593/"
        },
        {
            "id": "1098111389",
            "title": "Managing Cloud Native Data on Kubernetes",
            "subtitle": "Architecting Cloud Native Data Services Using Open Source Technology",
            "authors": "Jeff Carpenter, Patrick McFadin",
            "image": "https://www.dbooks.org/img/books/1098111389s.jpg",
            "url": "https://www.dbooks.org/managing-cloud-native-data-on-kubernetes-1098111389/"
        },
        {
            "id": "1912047446",
            "title": "An Introduction to C &amp; GUI Programming",
            "subtitle": "",
            "authors": "Simon Long",
            "image": "https://www.dbooks.org/img/books/1912047446s.jpg",
            "url": "https://www.dbooks.org/an-introduction-to-c-gui-programming-1912047446/"
        },
        {
            "id": "1711470546",
            "title": "Contemporary Mathematics",
            "subtitle": "",
            "authors": "Donna Kirk",
            "image": "https://www.dbooks.org/img/books/1711470546s.jpg",
            "url": "https://www.dbooks.org/contemporary-mathematics-1711470546/"
        },
        {
            "id": "1805110195",
            "title": "The Last Man Who Knew Everything",
            "subtitle": "Thomas Young",
            "authors": "Andrew Robinson",
            "image": "https://www.dbooks.org/img/books/1805110195s.jpg",
            "url": "https://www.dbooks.org/the-last-man-who-knew-everything-1805110195/"
        },
        {
            "id": "5685527822",
            "title": "HackSpace Magazine: Issue 65",
            "subtitle": "April 2023",
            "authors": "HackSpace Team",
            "image": "https://www.dbooks.org/img/books/5685527822s.jpg",
            "url": "https://www.dbooks.org/hackspace-magazine-issue-65-5685527822/"
        },
        {
            "id": "5685535457",
            "title": "Intro to Social Media",
            "subtitle": "",
            "authors": "Cheryl Lawson",
            "image": "https://www.dbooks.org/img/books/5685535457s.jpg",
            "url": "https://www.dbooks.org/intro-to-social-media-5685535457/"
        },
        {
            "id": "5679752518",
            "title": "HackSpace magazine: Issue 64",
            "subtitle": "March 2023",
            "authors": "HackSpace Team",
            "image": "https://www.dbooks.org/img/books/5679752518s.jpg",
            "url": "https://www.dbooks.org/hackspace-magazine-issue-64-5679752518/"
        },
        {
            "id": "5679742652",
            "title": "Introduction to Mechanical Engineering Design",
            "subtitle": "",
            "authors": "Jacqulyn A. Baughman",
            "image": "https://www.dbooks.org/img/books/5679742652s.jpg",
            "url": "https://www.dbooks.org/introduction-to-mechanical-engineering-design-5679742652/"
        },
        {
            "id": "1642002305",
            "title": "Svelte Succinctly",
            "subtitle": "",
            "authors": "Ed Freitas",
            "image": "https://www.dbooks.org/img/books/1642002305s.jpg",
            "url": "https://www.dbooks.org/svelte-succinctly-1642002305/"
        },
        {
            "id": "1800644124",
            "title": "Introduction to Systems Biology",
            "subtitle": "Workbook for Flipped-classroom Teaching",
            "authors": "Thomas Sauter, Marco Albrecht",
            "image": "https://www.dbooks.org/img/books/1800644124s.jpg",
            "url": "https://www.dbooks.org/introduction-to-systems-biology-1800644124/"
        },
        {
            "id": "111954601X",
            "title": "Blockchain For Dummies",
            "subtitle": "",
            "authors": "Manav Gupta",
            "image": "https://www.dbooks.org/img/books/111954601Xs.jpg",
            "url": "https://www.dbooks.org/blockchain-for-dummies-111954601x/"
        }
    ]

def populate_books():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        for book in books:
            try:
                cursor.execute('''
                    INSERT INTO books (id, title, subtitle, authors, image, url)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (book['id'], book['title'], book['subtitle'], book['authors'], book['image'], book['url']))
            except sqlite3.IntegrityError:
                print(f"Book with ID {book['id']} already exists.")
        conn.commit()
        print("Sample data added successfully!")

if __name__ == "__main__":
    populate_books()

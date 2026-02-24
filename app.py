from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

class MinistryOfInteriorApp:
    def __init__(self):
        self.app = app
        self.candidates = [
            {'id': 1, 'name': 'Martine Dupont', 'party': 'Parti Conservateur', 'votes': 0},
            {'id': 2, 'name': 'Jean-Luc Martin', 'party': 'Parti Républicain', 'votes': 0},
            {'id': 3, 'name': 'Marie Pierre', 'party': 'Parti Socialiste', 'votes': 0},
            {'id': 4, 'name': 'Pierre Leroy', 'party': 'Parti Écologiste', 'votes': 0},
            {'id': 5, 'name': 'Sophie Bernard', 'party': 'Indépendant', 'votes': 0}
        ]
    
    def init_app(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/vote', 'vote', self.vote, methods=['POST'])
        self.app.add_url_rule('/reset', 'reset', self.reset, methods=['POST'])
        self.app.add_url_rule('/results', 'results', self.results)
    
    def index(self):
        return render_template('index.html', candidates=self.candidates)
    
    def vote(self):
        candidate_id = request.form.get('candidate_id', type=int)
        if candidate_id and 1 <= candidate_id <= len(self.candidates):
            self.candidates[candidate_id-1]['votes'] += 1
        return redirect(url_for('results'))
    
    def reset(self):
        self.candidates = [
            {'id': 1, 'name': 'Martine Dupont', 'party': 'Parti Conservateur', 'votes': 0},
            {'id': 2, 'name': 'Jean-Luc Martin', 'party': 'Parti Républicain', 'votes': 0},
            {'id': 3, 'name': 'Marie Pierre', 'party': 'Parti Socialiste', 'votes': 0},
            {'id': 4, 'name': 'Pierre Leroy', 'party': 'Parti Écologiste', 'votes': 0},
            {'id': 5, 'name': 'Sophie Bernard', 'party': 'Indépendant', 'votes': 0}
        ]
        return redirect(url_for('results'))
    
    def results(self):
        total = sum(c['votes'] for c in self.candidates)
        percentages = [(c, c['votes'] / total * 100 if total > 0 else 0) for c in self.candidates]
        percentages.sort(key=lambda x: x[1], reverse=True)
        return render_template('results.html', candidates=self.candidates, percentages=percentages, total=total)

if __name__ == '__main__':
    ministry_app = MinistryOfInteriorApp()
    ministry_app.init_app()
    ministry_app.app.run(host='0.0.0.0', debug=True)
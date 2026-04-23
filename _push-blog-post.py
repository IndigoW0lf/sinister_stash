#!/usr/bin/env python3
"""
One-shot script: creates the "The Part Nobody Talks About at the Gun Store"
blog post in Field Notes on sinister-goods-2.myshopify.com.

Run from anywhere:
    python3 _push-blog-post.py

Delete this file after use — the token is passed via env var or hardcoded below.
"""

import json
import urllib.request
import urllib.error
import os
import sys

SHOP = "sinister-goods-2.myshopify.com"
TOKEN = os.environ.get("SHOPIFY_TOKEN", "")
if not TOKEN:
    print("Set SHOPIFY_TOKEN env var before running.")
    print("  export SHOPIFY_TOKEN=shpat_...")
    sys.exit(1)
API = f"https://{SHOP}/admin/api/2024-01"
HEADERS = {
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json",
}

BODY_HTML = """
<p>When I bought my first gun, I walked out with a firearm, a cable lock still in its plastic packaging, and approximately zero useful information about what came next.</p>

<p>The cable lock is sitting in a drawer somewhere. I know I'm not alone in that.</p>

<p>Gun culture has always been good at the exciting parts. The gear. The range etiquette. The debate about calibers that nobody ever fully resolves. What it has consistently skipped is the unglamorous stuff — the part where someone sits down and tells you, without condescension and without a political agenda, what responsible gun ownership actually requires.</p>

<p>That conversation is the one we're going to have here.</p>

<hr>

<h2>Safe storage. Let's start here.</h2>

<p>Approximately half of the guns used in suicides belong to the person who dies. Most guns accessed by children in accidents belong to someone in their household. Safe storage is not a debate. It is the most direct thing you can do to reduce the harm a gun in your home could cause to the people you love — including yourself.</p>

<p>Here's what that actually looks like, tiered by situation:</p>

<p><strong>If you're renting, live alone, or have no children in the house:</strong><br>
Your cable lock is the floor, not the ceiling. A biometric quick-access safe runs $50–150 and mounts inside a nightstand drawer. If your carry gun is accessible to you in an emergency, that's what matters — and it should be inaccessible to anyone else. That's the whole point.</p>

<p><strong>If you have children in the home:</strong><br>
A quick-access safe for your carry gun. A full-size locked safe or cabinet for everything else. Trigger locks on anything stored long-term. The statistics on children and household firearms are not abstract. Make it inaccessible. Full stop.</p>

<p><strong>If you carry daily:</strong><br>
Your carry gun is with you or in the safe. There is no "just left it on the counter" situation. A rapid-access safe on your nightstand handles the overnight question.</p>

<p>Free gun locks are available through the Project ChildSafe program. You can find a distribution site near you at <a href="https://projectchildsafe.org/safety/find-a-safety-kit" target="_blank" rel="noopener">projectchildsafe.org/safety/find-a-safety-kit</a>. No purchase required. No judgment. Just a lock.</p>

<hr>

<h2>Now the harder conversation.</h2>

<p>Sinister Stash exists for communities that mainstream gun culture forgot. Some of those communities are disproportionately affected by the statistic I cited above. LGBTQ+ people — particularly trans people — face dramatically elevated rates of suicidal ideation compared to the general population. That is the world we are operating in.</p>

<p>We are not going to pretend otherwise or bury a hotline number in a footer you'll never see.</p>

<p>If you are in a hard place right now, these people pick up:</p>

<ul>
  <li><strong>988 Suicide &amp; Crisis Lifeline:</strong> call or text 988, 24 hours</li>
  <li><strong>The Trevor Project</strong> (LGBTQ+ focused): 1-866-488-7386, or text START to 678-678</li>
  <li><strong>Crisis Text Line:</strong> text HOME to 741741</li>
  <li><strong>Trans Lifeline:</strong> 877-565-8860</li>
</ul>

<p>And if you're not in a hard place right now but you've been in one before, or you know someone who cycles in and out of one — the conversation about means restriction is worth having. Putting distance between a gun and a moment of crisis is one of the most evidence-based interventions that exists. That might look like a safe. It might look like asking a trusted person to store your firearms temporarily. It might look like something else entirely. You know your situation better than anyone.</p>

<p>Carrying this stuff is not a sign you shouldn't own a firearm. It's a sign you're paying attention.</p>

<hr>

<h2>The legal stuff. Quick version.</h2>

<p>First-time buyers often arrive without the informal knowledge network that grew-up-around-guns people inherit by default. Here are the things to know that nobody will tell you at the point of sale:</p>

<p><strong>Know your state's laws.</strong> Carry laws vary significantly by state. The NRA's state law summaries are one source — yes, them, because they're comprehensive regardless of your politics. USCCA also maintains a state law guide. Know what you're legally allowed to do before you do it.</p>

<p><strong>Safe transportation.</strong> In most states, transporting a firearm requires it to be unloaded and in a locked case. Know the rules for your state before you put your gun in your car.</p>

<p><strong>Universal background checks.</strong> If you purchase from a licensed dealer, you've already gone through a federal background check. Private sales laws vary by state. Know yours.</p>

<p>We support universal background checks, red flag laws, and safe storage legislation. That's not a political statement from this brand — it's consistent with owning responsibly and giving a damn about what happens in the broader world we live in.</p>

<hr>

<h2>One more thing, specifically for BIPOC gun owners.</h2>

<p>Legal carry does not guarantee safety from state violence. That is documented and we are not going to tell you otherwise.</p>

<p>Know Your Rights resources for interactions with law enforcement:</p>

<ul>
  <li><a href="https://www.aclu.org/know-your-rights" target="_blank" rel="noopener">ACLU's Know Your Rights guide</a></li>
  <li>If you carry, know your state's protocol for disclosing to law enforcement during a traffic stop — this varies by state and matters</li>
</ul>

<p>The presence of a firearm can escalate an already dangerous interaction with police. That is the reality. Knowing your rights and knowing your state's laws is the best available tool for navigating it. We hold the contradiction honestly: self-defense is a right, and that right does not protect you from everything.</p>

<hr>

<h2>The short version of all of this:</h2>

<p>You showed up. You made the decision. Now own it the whole way — which means the boring parts too. Safe storage. Knowing the laws. Taking care of yourself and the people around you.</p>

<p>That's what building it right looks like.</p>

<p>We talk about the stuff gun culture skips.</p>

<p><em>— Sinister Stash</em></p>

<hr>

<p><strong>Resources referenced in this post:</strong></p>
<ul>
  <li>Project ChildSafe free gun lock locator: <a href="https://projectchildsafe.org/safety/find-a-safety-kit" target="_blank" rel="noopener">projectchildsafe.org/safety/find-a-safety-kit</a></li>
  <li>988 Suicide &amp; Crisis Lifeline: call or text 988</li>
  <li>The Trevor Project: 1-866-488-7386 / text START to 678-678</li>
  <li>Crisis Text Line: text HOME to 741741</li>
  <li>Trans Lifeline: 877-565-8860</li>
  <li>ACLU Know Your Rights: <a href="https://www.aclu.org/know-your-rights" target="_blank" rel="noopener">aclu.org/know-your-rights</a></li>
</ul>
"""

ARTICLE = {
    "article": {
        "title": "The Part Nobody Talks About at the Gun Store",
        "handle": "the-part-nobody-talks-about",
        "body_html": BODY_HTML,
        "summary_html": "Safe storage, mental health resources, and the honest conversation about risk that gun culture skipped — specifically for queer, BIPOC, progressive, and first-time gun owners.",
        "tags": "How-To, Responsible Ownership, Field Notes, harm reduction, safe storage, mental health",
        "published": True,
    }
}


def api_get(path):
    req = urllib.request.Request(f"{API}{path}", headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def api_post(path, data):
    payload = json.dumps(data).encode()
    req = urllib.request.Request(f"{API}{path}", data=payload, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def main():
    print("Fetching blogs...")
    blogs = api_get("/blogs.json")["blogs"]
    for b in blogs:
        print(f"  [{b['id']}] {b['title']} — handle: {b['handle']}")

    field_notes = next(
        (b for b in blogs if "field" in b["title"].lower() or "field-notes" in b["handle"]),
        None,
    )

    if not field_notes:
        print("\nCouldn't auto-detect Field Notes. Available blogs above.")
        blog_id = input("Enter blog ID to post to: ").strip()
    else:
        blog_id = field_notes["id"]
        print(f"\nFound: {field_notes['title']} (id {blog_id})")

    print("Creating article...")
    result = api_post(f"/blogs/{blog_id}/articles.json", ARTICLE)
    article = result["article"]
    print(f"\nDone.")
    print(f"  Title:  {article['title']}")
    print(f"  Handle: {article['handle']}")
    print(f"  URL:    https://sinisterstash.com/blogs/{field_notes['handle']}/{article['handle']}")
    print(f"  Status: {'published' if article['published_at'] else 'draft'}")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()}")
        sys.exit(1)

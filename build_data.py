import json,csv,zipfile,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
prospects=json.loads((ROOT/'data/affiliate_seed.json').read_text(encoding='utf-8'))
# Seed product information is derived from verified Make scenario list and prepared catalog, not from sales.
products=[
('VAVE-AIC-01','Vave Viral Hook Lab',10005308,'Creator Lab',29,'Original hooks, short scripts and a review plan from one topic.','No publishing, trend feed or performance guarantee.'),
('VAVE-AIC-02','Vave AI UGC Ad Studio',10005309,'Creator Lab',39,'UGC-style ad concepts, scripts and shot directions.','Does not generate or publish video.'),
('VAVE-AIC-03','Vave AI Lead Magnet Builder',10005310,'Creator Lab',29,'Lead magnet text, worksheet, landing-page and email drafts.','Does not produce a designed PDF or host a signup page.'),
('VAVE-AIC-04','Vave AI YouTube Studio',10005312,'Creator Lab',29,'Publishing kit from a supplied original video transcript.','Does not upload videos or generate imagery.'),
('VAVE-AIC-05','Vave AI Product Outline Planner',10015651,'Creator Lab',39,'Product plan, sample worksheet and sales-copy draft.','Does not build software or publish a product.'),
('VAVE-AIC-06','Vave AI Voice Localization',10005313,'Creator Lab',39,'Localized scripts, captions and voiceover-ready text.','Does not synthesize audio or clone voices.'),
('VAVE-AIC-07','Vave Content Pattern Analyst',10015652,'Creator Lab',29,'Analyzes dated user-provided content examples into new ideas.','Does not fetch or monitor live trends.'),
('VAVE-AIC-08','Vave AI Ad Concept Research Desk',10015654,'Creator Lab',39,'Creative briefs and original concepts from submitted ad observations.','Does not access ad platforms or verify performance.'),
('VAVE-AIC-09','Vave AI Podcast Clip Selector',10005327,'Creator Lab',39,'Timestamp-based editorial clip suggestions from transcripts.','Does not cut, transcribe or render video.'),
('VAVE-AIC-10','Vave Faceless Video Storyboard Studio',10015656,'Creator Lab',59,'Scripts, storyboards, B-roll suggestions and production plans.','Does not render videos, images or voiceovers.'),
('VAVE-AIC-11','Vave Comment-to-DM Campaign Planner',10005328,'Creator Lab',29,'Manual configuration plan for keyword-triggered creator lead magnets.','Does not send DMs or connect to Instagram.'),
('VAVE-AIC-12','Vave AI Customer Support Draft Desk',10015657,'Creator Lab',49,'Support reply drafts based on an approved knowledge base.','Does not send email or access a CRM.'),
('VAVE-BIZ-01','Vave Content Repurposer',10004712,'Business',49,'Repurposing drafts and platform-tailored copy from a transcript.','Does not schedule or publish posts.'),
('VAVE-BIZ-02','Vave Social Content Planner',10004720,'Business',49,'Content plan based on a factual brand brief.','Does not use live analytics or post content.'),
('VAVE-BIZ-03','Vave Carousel and Reel Kit',10004722,'Business',49,'Carousel and reel scripts, production direction and checklists.','Does not render media.'),
('VAVE-BIZ-04','Vave Rent Roll Extractor',10004725,'Business',99,'Draft PDF extraction into a structured result for review.','Not a validated underwriting or autonomous accounting system.'),
('VAVE-BIZ-05','Vave Invoice Extractor',10004727,'Business',79,'Draft invoice-field extraction for review.','Not a validated accounting/bookkeeping system.'),
]
products=[{'id':sku,'name':name,'scenarioId':sid,'category':category,'price':price,'pitch':pitch,'limits':limits,'stage':'Development','blueprint':False,'importTest':False,'runtimeTest':False,'listingApproved':False,'storeUrl':'','owner':'Vave','nextAction':'Review config → export genuine blueprint → authorized QA','notes':'Proposed price; not a live Gumroad listing.'} for sku,name,sid,category,price,pitch,limits in products]
# Build a useful initial local work queue. Complete statuses refer only to preparatory work.
def task(id,title,area,status,priority,detail):return {'id':id,'title':title,'area':area,'status':status,'priority':priority,'detail':detail,'due':'','owner':'Vave','link':''}
tasks=[
 task('TASK-01','Build 17 Make development scenarios','Products','Done','P0','17 scenarios currently inactive; no proof of live functionality.'),
 task('TASK-02','Reconcile catalog with Make IDs','Products','Done','P0','Scenario IDs and product limitations documented.'),
 task('TASK-03','Finish Gemini configuration audit','Products','In progress','P0','Review all models and response paths without running scenarios.'),
 task('TASK-04','Export real Viral Hook Lab blueprint','Products','Blocked','P0','Needs actual export; internal specs are not buyer blueprints.'),
 task('TASK-05','Import and test first product','Products','Blocked','P0','Requires Make execution capacity and explicit authorization.'),
 task('TASK-06','Create Gumroad product drafts','Store','Blocked','P0','Requires authenticated seller access; do not publish unverified items.'),
 task('TASK-07','Verify Gumroad Pages custom home','Store','Blocked','P1','Account feature availability and sanitizer preview are unconfirmed.'),
 task('TASK-08','Approve brand + product cover system','Store','In progress','P1','Midnight blue storefront direction prepared; verify actual seller assets.'),
 task('TASK-09','Qualify first 10 affiliate candidates','Affiliates','To do','P0','Reconfirm audience, current activity, contact and conflict.'),
 task('TASK-10','Prepare affiliate commission economics','Affiliates','In progress','P1','60% owner-set affiliate rate; not yet configured or active on Gumroad.'),
 task('TASK-11','Activate Vave Dispatch opt-in','Email','Blocked','P1','Requires seller access, platform eligibility and policy review.'),
 task('TASK-12','Finalize seven email drafts','Email','Done','P2','Prepared, unsent; live links must be verified.'),
 task('TASK-13','Build first qualified client-lead list','Clients','To do','P0','Separate store-related implementation buyers from other company CRM.'),
 task('TASK-14','Write 3 narrow client offers','Clients','To do','P1','Creator ops, PDF extraction, and small-business admin.'),
 task('TASK-15','Create product demonstration recording','Marketing','Blocked','P1','Requires genuine tested run/results.'),
 task('TASK-16','Create 14-day launch content plan','Marketing','Done','P2','Draft planning prepared; no posts published.'),
 task('TASK-17','Set up support address, policies and payout','Operations','Blocked','P0','Owner-controlled seller configuration is unresolved.'),
 task('TASK-18','Confirm public-safe GitHub deployment boundary','Operations','To do','P0','Local browser CRM contains contact/notes; never publish backups.'),
]
content=[
 {'id':'CNT-01','title':'Why most hook generators disappoint','channel':'TikTok / Reels','format':'Short video','stage':'Draft','product':'Vave Viral Hook Lab','cta':'Free hook checklist','publishDate':'','notes':'Demonstrate real output after product QA.'},
 {'id':'CNT-02','title':'What a Make blueprint actually includes','channel':'YouTube / Reels','format':'Tutorial','stage':'Draft','product':'Vave Content Repurposer','cta':'Useful educational video','publishDate':'','notes':'Explain connection setup truthfully.'},
 {'id':'CNT-03','title':'From one topic to a week of content','channel':'Instagram','format':'Carousel','stage':'Draft','product':'Vave Social Content Planner','cta':'Join Vave Dispatch','publishDate':'','notes':'No fabricated performance results.'},
 {'id':'CNT-04','title':'How a simple invoice workflow is scoped','channel':'LinkedIn','format':'Educational post','stage':'Draft','product':'Vave Invoice Extractor','cta':'Request demo after QA','publishDate':'','notes':'Do not imply it is an accounting replacement.'},
 {'id':'CNT-05','title':'Behind the build: Vave workflows','channel':'TikTok / Reels','format':'Behind the scenes','stage':'Draft','product':'Vave Viral Hook Lab','cta':'Follow launch updates','publishDate':'','notes':'Show interface and honest status.'},
]
zip_path=Path('/mnt/data/Vave_2026-10-22_Night_Sprint.zip')
emails=[]
with zipfile.ZipFile(zip_path) as z:
    entries=sorted((n for n in z.namelist() if re.search(r'/05_Email_Campaign/0[1-7]_[^/]+\.md$',n)))
    labels=['New subscriber welcome','Practical lesson (day 2)','Free resource (day 5)','Verified launch alert','Subscriber coupon','Buyer onboarding','Affiliate onboarding']
    for i,path in enumerate(entries):
        txt=z.read(path).decode('utf-8')
        subject=re.search(r'^# Subject:\s*(.+)',txt,re.M)
        emails.append({'id':f'EM-{i+1:02d}','name':labels[i],'segment':['Followers','Followers','Followers','Followers','Followers','Customers','Affiliates'][i],'subject':subject.group(1) if subject else labels[i],'body':txt.split('\n',1)[1].split('\n---\n')[0].strip(),'status':'Draft','schedule':'','purpose':['Welcome','Education','Resource','Launch','Promotion','Onboarding','Onboarding'][i],'notes':'Draft; requires verified links and activation approval.'})
partners=[]
clients=[]
resources=[
 {'name':'Vave Drive HQ','type':'Google Drive','href':'https://drive.google.com/drive/folders/19O-BgH3IllHi2_qbvMpQ1DJXt_lDB_4q','description':'Shared department structure; not a live sync.'},
 {'name':'Connected Make scenarios','type':'Make','href':'https://eu2.make.com/715909/scenarios','description':'Authoritative scenario workspace; sign-in required.'},
 {'name':'Affiliate public evidence list','type':'Local file','href':'assets/resources/Affiliate_Public_Source_List.csv','description':'28 sourced creator entries without private contact details.'},
 {'name':'Hook Quality Checklist','type':'Local file','href':'assets/resources/Vave_Hook_Quality_Checklist_FREE.pdf','description':'Free lead magnet; not yet a verified Gumroad product.'},
 {'name':'Gumroad Pages candidate','type':'Local file','href':'assets/resources/VAVE_GUMROAD_PROFILE_PREVIEW.html','description':'Earlier HTML storefront candidate; deployment unverified.'},
 {'name':'Release checklist','type':'Local file','href':'assets/resources/RECONCILED_YESTERDAY_CHECKLIST.md','description':'Previous confirmed vs pending launch work.'},
 {'name':'Affiliate & partner playbook','type':'Local file','href':'docs/AFFILIATE_AND_PARTNER_GROWTH.md','description':'Qualified creator recruiting and activation procedures.'},
 {'name':'Client acquisition playbook','type':'Local file','href':'docs/CLIENT_ACQUISITION_PLAYBOOK.md','description':'Store-specific implementation prospecting and scoped offers.'},
 {'name':'Vave Dispatch email plan','type':'Local file','href':'docs/VAVE_DISPATCH_EMAIL_PLAN.md','description':'Consent-based lifecycle strategy and audience segments.'},
 {'name':'Security & deployment guide','type':'Local file','href':'docs/SECURITY_AND_DEPLOYMENT.md','description':'How to protect data when hosting or connecting integrations.'},
]
seed={'asOf':'2026-11-02','products':products,'affiliates':prospects,'emails':emails,'partners':partners,'clients':clients,'tasks':tasks,'content':content,'resources':resources}
(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets/data.js').write_text('window.VAVE_SEED = '+json.dumps(seed,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
(ROOT/'data/seed.json').write_text(json.dumps(seed,ensure_ascii=False,indent=2),encoding='utf-8')
with (ROOT/'assets/resources/Affiliate_Public_Source_List.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['Creator','Niche','Tier','Evidence URL','Status'])
    for r in prospects:w.writerow([r['name'],r['niche'],r['tier'],r['source'],r['stage']])
print(f'Wrote seed: {len(products)} products, {len(prospects)} affiliates, {len(emails)} email drafts, {len(tasks)} tasks')
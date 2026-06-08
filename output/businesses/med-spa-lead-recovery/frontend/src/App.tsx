import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import LeadLeakCalculator from './views/LeadLeakCalculator';
import InstagramDMFlow from './views/InstagramDMFlow';
import FreeLeadAuditForm from './views/FreeLeadAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'lead-leak-calculator': LeadLeakCalculator,
  'instagram-d-m-flow': InstagramDMFlow,
  'free-lead-audit-form': FreeLeadAuditForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('lead-leak-calculator')} className={route === 'lead-leak-calculator' ? 'active' : ''}>LeadLeakCalculator</button>
          <button onClick={() => setRoute('instagram-d-m-flow')} className={route === 'instagram-d-m-flow' ? 'active' : ''}>InstagramDMFlow</button>
          <button onClick={() => setRoute('free-lead-audit-form')} className={route === 'free-lead-audit-form' ? 'active' : ''}>FreeLeadAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }

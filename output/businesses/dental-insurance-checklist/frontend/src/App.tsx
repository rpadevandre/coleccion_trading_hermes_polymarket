import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import ChecklistDemo from './views/ChecklistDemo';
import ReworkCalculator from './views/ReworkCalculator';
import OfficeAuditForm from './views/OfficeAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'checklist-demo': ChecklistDemo,
  'rework-calculator': ReworkCalculator,
  'office-audit-form': OfficeAuditForm,
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
          <button onClick={() => setRoute('checklist-demo')} className={route === 'checklist-demo' ? 'active' : ''}>ChecklistDemo</button>
          <button onClick={() => setRoute('rework-calculator')} className={route === 'rework-calculator' ? 'active' : ''}>ReworkCalculator</button>
          <button onClick={() => setRoute('office-audit-form')} className={route === 'office-audit-form' ? 'active' : ''}>OfficeAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
